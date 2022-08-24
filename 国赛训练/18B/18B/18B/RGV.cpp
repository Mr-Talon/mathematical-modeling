#include "stdafx.h"
#include "RGV.h"
#define STEP1 18    //RGV�ƶ�1����λ����ʱ��
#define STEP2 32	//RGV�ƶ�2����λ����ʱ��
#define STEP3 46		//RGV�ƶ�3����λ����ʱ��	
#define CNC_WORKTIME 545		//CNC�ӹ����һ��һ���������������ʱ��
#define CNC1 27		//RGVΪCNC1#��3#��5#��7#һ������������ʱ��
#define CNC0 32		//RGVΪCNC2#��4#��6#��8#һ������������ʱ��
#define CLEAN 25		//RGV���һ�����ϵ���ϴ��ҵ����ʱ��
#define CNCNUMBER 8
using namespace std;


int n = 0;     //�ӹ������к�
RGV::RGV()
{
	position = 0;
	now_cnc = 1;
	rgv_flag = 0;
	time = 0;
	sum = 0;
}


void RGV::Init(CNC* p)   //pΪCNC����ָ��
//��ʼ��  ����˳���������
{
	CNC* ptr = p;
	for (int i = 0; i < CNCNUMBER; i++, now_cnc++) {
		int temp = posCalculate(position, (p + now_cnc - 1)->position);

		if (temp) {
			time += temp;      //RGV�ƶ�������ʱ��
			//���ƶ���ͬʱ����CNC�Ĺ���ʱ����Ҫ����
			CNC* ptr1 = p;
			for (int i = 0; i < CNCNUMBER; i++, ptr1++) {
				ptr1->countdown(temp);
			}
		}
		load(p);
		position = (p + now_cnc - 1)->position;
	}
}


int RGV::posCalculate(int pos1, int pos2)  //RGV�ƶ�ʱ�����
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
//�����㷨 RGV�ƶ�   ̰�ķ���RGV�����ܹ���������
{
	CNC* ptr = p;
	int time1 = 10000;//����ʱ��
	int time2 = 0;    //��ǰʱ��
	int next_cnc = 1; //���Ž�
	for (int i = 0; i < CNCNUMBER; i++, ptr++)
	{
		int postime = posCalculate(position, ptr->position);
		time2 = ptr->count + postime;   //CNC����ʣ��ʱ�� + RGV�ƶ�����ǰλ��ʱ��
		if (time1 > time2) {
			time1 = time2;
			next_cnc = ptr->number;
		}
		else continue;
	}

	if (now_cnc != next_cnc) {   //��ǰ���������Ŷ���RGV�ƶ�
		int temp = posCalculate(position, (p + next_cnc - 1)->position);

		if (temp) {
			time += temp;   //RGV�ƶ�ʱ��
			//RGV�ƶ�������������CNC�Ĺ���ʣ��ʱ����Ҫ����
			CNC* ptr1 = p;
			for (int i = 0; i < CNCNUMBER; i++, ptr1++) //����CNCʣ��ʱ�� - rgv�ƶ�ʱ��
			{
				ptr1->countdown(temp);
			}
		}
		position = (p + next_cnc - 1)->position;
		now_cnc = next_cnc;
	}
	wait(p);
}


void RGV::load(CNC* p)//RGV������
{
	CNC* ptr = p + now_cnc - 1; //�˴������±��CNC���Ҫע�⣡
	int temp = 0;

	cout << time << '\t' << '\t' << ptr->n << '\t' << '\t' << ++n << '\t' << now_cnc << endl;
	if ((ptr->number % 2) == 1) {
		temp = CNC1;
	}
	else {
		temp = CNC0;
	}
	time += temp;   //����ǰCNC���� ���ѵ�ʱ��
	CNC* ptr1 = p;

	//���ϵ�ͬʱ ����CNC�ڼӹ� ����ÿ����ʱ��
	for (int i = 0; i < CNCNUMBER; i++, ptr1++) //����CNCʣ��ʱ�� - rgv�ƶ�ʱ��
	{
		ptr1->countdown(temp);
	}
	ptr->n = n;  //��ǵ�ǰCNC�ӹ������
	ptr->count = CNC_WORKTIME;   //��ǵ�ǰCNC�ӹ���ʱ��
	rgv_flag = 1;
}


void RGV::clean(CNC* p)//RGV��ϴ
{
	sum++;
	int temp = CLEAN;
	time += temp;   //��������ʱ��
	//�����ͬʱ ����CNC��ʣ�๤��ʱ��Ҫ����
	CNC* ptr1 = p;
	for (int i = 0; i < CNCNUMBER; i++, ptr1++) //����CNCʣ��ʱ�� - rgv�ƶ�ʱ��
	{
		ptr1->countdown(temp);
	}
}
void RGV::wait(CNC* p)
{
	CNC* ptr = p + now_cnc - 1;
	// ���RGV�ߵ���Ӧ��CNC��ǰCNC��û�й������  ����Ҫ�ȴ�
	if (ptr->count) {
		int temp = ptr->count;
		time += temp;
		CNC* ptr1 = p;
		for (int i = 0; i < CNCNUMBER; i++, ptr1++) //����CNCʣ��ʱ�� - rgv�ƶ�ʱ��
		{
			ptr1->countdown(temp);
		}
		ptr->count = 0;
	}
	else return;
}