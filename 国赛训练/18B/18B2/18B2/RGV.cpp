#include "stdafx.h"
#include "RGV.h"
#define STEP1 18    //RGV�ƶ�1����λ����ʱ��
#define STEP2 32   //RGV�ƶ�2����λ����ʱ��
#define STEP3 46   //RGV�ƶ�3����λ����ʱ��
#define CNC_WORKTIME1 455    //CNC�ӹ����һ�������������ϵĵ�һ����������ʱ��
#define CNC_WORKTIME2 182//CNC�ӹ����һ�������������ϵĵڶ�����������ʱ��
#define CNC1 27    //RGVΪCNC1#��3#��5#��7#һ������������ʱ��
#define CNC0 32    //RGVΪCNC2#��4#��6#��8#һ������������ʱ��
#define CLEAN 25    //RGV���һ�����ϵ���ϴ��ҵ����ʱ��
#define CNC_NUMBER 8
#define TIME 28800
using namespace std;


int n = 0;//�ӹ������

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
		if (ptr->knife == 1) {  //��һ��ֻ�ܸ��е���1��CNC����
			int temp = posCalculate(position, (p + now_cnc - 1)->position);   //RGV���ߵ���Ӧ��CNC

			if (temp) {
				time += temp;
				CNC* ptr1 = p;
				for (int i = 0; i < CNC_NUMBER; i++, ptr1++) //ͬ��RGV��CNC��ʱ��
				{
					ptr1->countdown(temp);
				}
			}

			load(p);   //����
			position = (p + now_cnc - 1)->position;    //RGV��λ�ñ仯
			rgv_flag = 1;     //��ʼ�ִ� RGV��״̬���ǿ���
		}
		else continue;
	}
}


int RGV::posCalculate(int pos1, int pos2)
//����ʱ��͵�һ��û�б仯
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
// RGV��һ�������CNC��Ѱ���㷨   ̰���㷨
{
	CNC* ptr = p;
	int next_cnc = 1;//���Ž�
	int min_time1 = 1000;
	int now_time1 = 0;
	if (rgv_flag == 1) {
		for (int i = 0; i < CNC_NUMBER; i++, ptr++) {//  RGV���мȿ�ѡ�񵶾�1��Ҳ��ѡ�񵶾�2
			int postime = posCalculate(position, ptr->position);
			now_time1 = (ptr->count > postime) ? ptr->count : postime;
			if (min_time1 > now_time1) {
				min_time1 = now_time1;
				next_cnc = ptr->number;
			}
			else continue;
		}
	}
	else {//RGV�������Ű��Ʒ   ֻ��ȥѰ�ҵ���2��CNC
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


void RGV::move(CNC* p)//RGV�ƶ�
{
	int next_cnc = find(p);
	if (next_cnc != now_cnc) {//��ǰ���������Ŷ����ƶ�
		int temp = posCalculate(position, (p + next_cnc - 1)->position);
		if (temp) {
			time += temp;
			CNC* ptr1 = p;
			for (int i = 0; i < CNC_NUMBER; i++, ptr1++) //����CNCʣ��ʱ�� - rgv�ƶ�ʱ��
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
	// RGV���е���Ӧ��CNC�����Ĺ�����
	// �����ǰCNC��1�ŵ�   ����Ҫ���ľ�������CNC�İ��Ʒ����ʼ���ð��Ʒ�����0 ����û�У����ҽ����Ϸŵ�CNC�ϼӹ�
	// �����ǰCNC��2�ŵ�   ����Ҫ���ľ��� �����Ʒ�͸�CNC�ӹ�  RGV��ɿ���״̬
	CNC* ptr = p + now_cnc - 1; //�˴������±��CNC���Ҫע�⣡

	//���µ�ǰCNC��RGV������
	int count_temp = 0;
	if (ptr->knife == 1) {  //����1��CNC
		cout << time << '\t' << rgv_flag << '\t' << ptr->n << '\t' << '\t' << ++n << '\t' << '\t' << now_cnc << endl;
		count_temp = CNC_WORKTIME1;
		rgv_flag = 2;  //RGV�õ����Ʒ ״̬�����仯
		rgv_n = ptr->n;//���Ʒ���к�
		ptr->n = n;  //CNC���ڼӹ������µ�����
	}
	else {   //����2��CNC
		cout << time << '\t' << rgv_flag << '\t' << ptr->n << '\t' << '\t' << rgv_n << '\t' << '\t' << now_cnc << endl;
		count_temp = CNC_WORKTIME2 + CLEAN;
		rgv_flag = 1;   //RGV�õ���Ʒ ״̬�����仯
		if ((TIME - time) > CNC0 && (TIME - time) > CNC1) {
			sum = ptr->n;
		}
		else
			sum = (ptr->n - 1);   //RGV�ļӹ������仯
		ptr->n = rgv_n;          //CNC��ǰ�ӹ�������
	}
	ptr->count = count_temp;        

	//��������Ҫ��ʱ��
	int temp = 0;
	if ((ptr->number % 2) == 1) {
		temp = CNC1;
	}
	else {
		temp = CNC0;
	}
	time += temp;

	// �����Ϲ���������CNC�ӹ�����
	CNC* ptr1 = p;
	for (int i = 0; i < CNC_NUMBER; i++, ptr1++) //����CNCʣ��ʱ�� - rgv�ƶ�ʱ��
	{
		ptr1->countdown(temp);
	}
}


void RGV::wait(CNC* p)
//�͵�һ�����û�б仯
{
	CNC* ptr = p + now_cnc - 1;
	if (ptr->count) {
		int temp = ptr->count;
		time += temp;
		CNC* ptr1 = p;
		for (int i = 0; i < CNC_NUMBER; i++, ptr1++) //����CNCʣ��ʱ�� - rgv�ƶ�ʱ��
		{
			ptr1->countdown(temp);
		}
	}
	else return;
}