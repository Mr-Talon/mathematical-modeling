#include "stdafx.h"
#include "RGV.h"
#define STEP1 18    //RGV移动1个单位所需时间
#define STEP2 32	//RGV移动2个单位所需时间
#define STEP3 46		//RGV移动3个单位所需时间	
#define CNC_WORKTIME 545		//CNC加工完成一个一道工序的物料所需时间
#define CNC1 27		//RGV为CNC1#，3#，5#，7#一次上下料所需时间
#define CNC0 32		//RGV为CNC2#，4#，6#，8#一次上下料所需时间
#define CLEAN 25		//RGV完成一个物料的清洗作业所需时间
#define CNCNUMBER 8
using namespace std;


int n = 0;     //加工物序列号
RGV::RGV()
{
	position = 0;
	now_cnc = 1;
	rgv_flag = 0;
	time = 0;
	sum = 0;
}


void RGV::Init(CNC* p)   //p为CNC数组指针
//初始化  按照顺序操作即可
{
	CNC* ptr = p;
	for (int i = 0; i < CNCNUMBER; i++, now_cnc++) {
		int temp = posCalculate(position, (p + now_cnc - 1)->position);

		if (temp) {
			time += temp;      //RGV移动花费了时间
			//在移动的同时所有CNC的工作时间需要减掉
			CNC* ptr1 = p;
			for (int i = 0; i < CNCNUMBER; i++, ptr1++) {
				ptr1->countdown(temp);
			}
		}
		load(p);
		position = (p + now_cnc - 1)->position;
	}
}


int RGV::posCalculate(int pos1, int pos2)  //RGV移动时间计算
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


void RGV::move(CNC* p)
//调度算法 RGV移动   贪心法：RGV最先能够到达优先
{
	CNC* ptr = p;
	int time1 = 10000;//最少时间
	int time2 = 0;    //当前时间
	int next_cnc = 1; //最优解
	for (int i = 0; i < CNCNUMBER; i++, ptr++)
	{
		int postime = posCalculate(position, ptr->position);
		time2 = ptr->count + postime;   //CNC工作剩余时间 + RGV移动到当前位置时间
		if (time1 > time2) {
			time1 = time2;
			next_cnc = ptr->number;
		}
		else continue;
	}

	if (now_cnc != next_cnc) {   //当前对象不是最优对象，RGV移动
		int temp = posCalculate(position, (p + next_cnc - 1)->position);

		if (temp) {
			time += temp;   //RGV移动时间
			//RGV移动过程中其他的CNC的工作剩余时间需要减掉
			CNC* ptr1 = p;
			for (int i = 0; i < CNCNUMBER; i++, ptr1++) //所有CNC剩余时间 - rgv移动时间
			{
				ptr1->countdown(temp);
			}
		}
		position = (p + next_cnc - 1)->position;
		now_cnc = next_cnc;
	}
	wait(p);
}


void RGV::load(CNC* p)//RGV上下料
{
	CNC* ptr = p + now_cnc - 1; //此处数组下标和CNC编号要注意！
	int temp = 0;

	cout << time << '\t' << '\t' << ptr->n << '\t' << '\t' << ++n << '\t' << now_cnc << endl;
	if ((ptr->number % 2) == 1) {
		temp = CNC1;
	}
	else {
		temp = CNC0;
	}
	time += temp;   //给当前CNC上料 花费的时间
	CNC* ptr1 = p;

	//上料的同时 其他CNC在加工 剪掉每个的时间
	for (int i = 0; i < CNCNUMBER; i++, ptr1++) //所有CNC剩余时间 - rgv移动时间
	{
		ptr1->countdown(temp);
	}
	ptr->n = n;  //标记当前CNC加工的物件
	ptr->count = CNC_WORKTIME;   //标记当前CNC加工的时间
	rgv_flag = 1;
}


void RGV::clean(CNC* p)//RGV清洗
{
	sum++;
	int temp = CLEAN;
	time += temp;   //增加清理时间
	//清理的同时 其他CNC的剩余工作时间要减掉
	CNC* ptr1 = p;
	for (int i = 0; i < CNCNUMBER; i++, ptr1++) //所有CNC剩余时间 - rgv移动时间
	{
		ptr1->countdown(temp);
	}
}
void RGV::wait(CNC* p)
{
	CNC* ptr = p + now_cnc - 1;
	// 如果RGV走到对应的CNC面前CNC还没有工作完成  就需要等待
	if (ptr->count) {
		int temp = ptr->count;
		time += temp;
		CNC* ptr1 = p;
		for (int i = 0; i < CNCNUMBER; i++, ptr1++) //所有CNC剩余时间 - rgv移动时间
		{
			ptr1->countdown(temp);
		}
		ptr->count = 0;
	}
	else return;
}