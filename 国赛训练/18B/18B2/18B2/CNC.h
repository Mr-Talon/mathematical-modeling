#pragma once

class CNC
{
private:
	int number;   //CNC���
	int position; //CNCλ��
	int knife;    //CNC�����ͺ�,1��һ������2�ڶ�������
	int count;    //CNCʣ�๤��ʱ��
	int n;        //�ӹ������к�
public:
	CNC();
	CNC(int num, int pos, int kni);
	void countdown(int temp);
	friend class RGV;
};
