#pragma once
#include "CNC.h"
class RGV
{
private:
	int position; //rgv��ǰλ��
	int now_cnc;   //��ǰĿ��
	int rgv_flag;  //rgv_flag,1������,0��

public:
	int time; //����ʱ
	int sum; //�ӹ���������

	RGV();
	void Init(CNC* p); //��һ�ֳ�ʼ��
	int posCalculate(int pos1, int pos2); //����RGV�ƶ�ʱ��
	void move(CNC* p); //RGV�ƶ�
	void load(CNC* p); //RGV������
	void clean(CNC* p);//RGV��ϴ
	void wait(CNC* p);//RGV�ȴ�
};
