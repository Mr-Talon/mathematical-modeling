#pragma once
#include "CNC.h"
using namespace std;
class RGV
{
private:
	int position;	//rgv��ǰλ��
	int now_cnc;	//rgv��ǰCNC����
	int rgv_flag;	//RGV��ǰ״̬��1���У�2���а��Ʒ
	int rgv_n;		//RGV��ǰ���Ʒ��
public:
	int time; //����ʱ
	int sum; //�ӹ���������

	RGV();
	int find(CNC* p); //Ѱ�����Ž�
	void Init(CNC* p); //��һ�ֳ�ʼ��
	int posCalculate(int pos1, int pos2); //����RGV�ƶ�ʱ��
	void move(CNC* p); //RGV�ƶ�
	void load(CNC* p); //RGV������
	void wait(CNC* p);//RGV�ȴ�
};
