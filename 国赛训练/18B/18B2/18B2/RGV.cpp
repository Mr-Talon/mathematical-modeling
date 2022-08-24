#include "stdafx.h"
#include "RGV.h"
#define STEP1 18    //RGV移动1个单位所需时间
#define STEP2 32   //RGV移动2个单位所需时间
#define STEP3 46   //RGV移动3个单位所需时间
#define CNC_WORKTIME1 455    //CNC加工完成一个两道工序物料的第一道工序所需时间
#define CNC_WORKTIME2 182//CNC加工完成一个两道工序物料的第二道工序所需时间
#define CNC1 27    //RGV为CNC1#，3#，5#，7#一次上下料所需时间
#define CNC0 32    //RGV为CNC2#，4#，6#，8#一次上下料所需时间
#define CLEAN 25    //RGV完成一个物料的清洗作业所需时间
#define CNC_NUMBER 8
#define TIME 28800
using namespace std;


int n = 0;//加工物序号

RGV::RGV()
{
	position = 0;
	now_cnc = 1;
	rgv_flag = 1;
	rgv_n = 0;
	time = 0;
	sum = 0;

	n = 0;
}


void RGV::Init(CNC* p)
{
	CNC* ptr = p;
	for (int i = 0; i < CNC_NUMBER; i++, ptr++, now_cnc++)
	{
		if (ptr->knife == 1) {  //第一轮只能给有刀具1的CNC上料
			int temp = posCalculate(position, (p + now_cnc - 1)->position);   //RGV行走到对应的CNC

			if (temp) {
				time += temp;
				CNC* ptr1 = p;
				for (int i = 0; i < CNC_NUMBER; i++, ptr1++) //同步RGV和CNC的时间
				{
					ptr1->countdown(temp);
				}
			}

			load(p);   //上料
			position = (p + now_cnc - 1)->position;    //RGV的位置变化
			rgv_flag = 1;     //初始轮次 RGV的状态都是空闲
		}
		else continue;
	}
}


int RGV::posCalculate(int pos1, int pos2)
//计算时间和第一问没有变化
{
	switch (abs(pos1 - pos2))
	{
	case 3: return STEP3;
	case 2: return STEP2;
	case 1: return STEP1;
	case 0: return 0;
	default: return ERROR;
	}
}


int RGV::find(CNC* p)
// RGV下一个服务的CNC的寻找算法   贪心算法
{
	CNC* ptr = p;
	int next_cnc = 1;//最优解
	int min_time1 = 1000;
	int now_time1 = 0;
	if (rgv_flag == 1) {
		for (int i = 0; i < CNC_NUMBER; i++, ptr++) {//  RGV空闲既可选择刀具1，也可选择刀具2
			int postime = posCalculate(position, ptr->position);
			now_time1 = (ptr->count > postime) ? ptr->count : postime;
			if (min_time1 > now_time1) {
				min_time1 = now_time1;
				next_cnc = ptr->number;
			}
			else continue;
		}
	}
	else {//RGV手上拿着半成品   只能去寻找刀具2的CNC
		for (int i = 0; i < CNC_NUMBER; i++, ptr++) {
			if (ptr->knife == 2) {
				int postime = posCalculate(position, ptr->position);
				now_time1 = (ptr->count > postime) ? ptr->count : postime;
				if (min_time1 > now_time1) {
					min_time1 = now_time1;
					next_cnc = ptr->number;
				}
			}
			else continue;
		}
	}
	return next_cnc;
}


void RGV::move(CNC* p)//RGV移动
{
	int next_cnc = find(p);
	if (next_cnc != now_cnc) {//当前对象不是最优对象，移动
		int temp = posCalculate(position, (p + next_cnc - 1)->position);
		if (temp) {
			time += temp;
			CNC* ptr1 = p;
			for (int i = 0; i < CNC_NUMBER; i++, ptr1++) //所有CNC剩余时间 - rgv移动时间
			{
				ptr1->countdown(temp);
			}
		}
		position = (p + next_cnc - 1)->position;
		now_cnc = next_cnc;
	}
	wait(p);
}


void RGV::load(CNC* p)
{
	// RGV运行到对应的CNC所做的工作：
	// 如果当前CNC是1号刀   那需要做的就是拿下CNC的半成品（初始调用半成品编号是0 就是没有）并且将生料放到CNC上加工
	// 如果当前CNC是2号刀   那需要做的就是 将半成品送给CNC加工  RGV变成空闲状态
	CNC* ptr = p + now_cnc - 1; //此处数组下标和CNC编号要注意！

	//更新当前CNC和RGV的属性
	int count_temp = 0;
	if (ptr->knife == 1) {  //工序1的CNC
		cout << time << '\t' << rgv_flag << '\t' << ptr->n << '\t' << '\t' << ++n << '\t' << '\t' << now_cnc << endl;
		count_temp = CNC_WORKTIME1;
		rgv_flag = 2;  //RGV拿到半成品 状态发生变化
		rgv_n = ptr->n;//半成品序列号
		ptr->n = n;  //CNC现在加工的是新的生料
	}
	else {   //工序2的CNC
		cout << time << '\t' << rgv_flag << '\t' << ptr->n << '\t' << '\t' << rgv_n << '\t' << '\t' << now_cnc << endl;
		count_temp = CNC_WORKTIME2 + CLEAN;
		rgv_flag = 1;   //RGV拿到成品 状态发生变化
		if ((TIME - time) > CNC0 && (TIME - time) > CNC1) {
			sum = ptr->n;
		}
		else
			sum = (ptr->n - 1);   //RGV的加工总数变化
		ptr->n = rgv_n;          //CNC当前加工的物料
	}
	ptr->count = count_temp;        

	//上下料需要的时间
	int temp = 0;
	if ((ptr->number % 2) == 1) {
		temp = CNC1;
	}
	else {
		temp = CNC0;
	}
	time += temp;

	// 上下料过程中其他CNC加工进程
	CNC* ptr1 = p;
	for (int i = 0; i < CNC_NUMBER; i++, ptr1++) //所有CNC剩余时间 - rgv移动时间
	{
		ptr1->countdown(temp);
	}
}


void RGV::wait(CNC* p)
//和第一问相比没有变化
{
	CNC* ptr = p + now_cnc - 1;
	if (ptr->count) {
		int temp = ptr->count;
		time += temp;
		CNC* ptr1 = p;
		for (int i = 0; i < CNC_NUMBER; i++, ptr1++) //所有CNC剩余时间 - rgv移动时间
		{
			ptr1->countdown(temp);
		}
	}
	else return;
}