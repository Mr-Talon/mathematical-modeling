#pragma once
class CNC
{
private:
	int number;   //CNC���   1-8
	int position; //CNCλ��     0-3
	int count;    //CNCʣ�๤��ʱ��
	int n;        //�ӹ������к�
public:
	CNC(int num, int pos);
	void countdown(int tem);
	friend class RGV;
};
