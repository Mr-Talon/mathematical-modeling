#include "stdafx.h"
#include "RGV.h"
#include "CNC.h"

#define CNCNUMBER 8
#define TIME 28800
using namespace std;
int main()
{
	RGV rgv;   //����RGV����
	CNC cnc[CNCNUMBER] = {   // ����CNC��������
		CNC(1,0), CNC(2,0), CNC(3,1), CNC(4,1),
		CNC(5,2), CNC(6,2), CNC(7,3), CNC(8,3) };
	CNC* pCNC = cnc;  //CNC����ָ��

	cout << "ʱ��" << '\t' << "���Ͽ�ʼ" << '\t' << "���Ͽ�ʼ" << '\t' << "CNC#" << endl;

	/*��һ��
	���迼��RGV���ƶ����͡������ϡ�����*/
	rgv.Init(pCNC);

	/*��(n+1)��
	RGVѭ�����ƶ������������ϡ��͡���ϴ������*/
	while (rgv.time <= TIME)
	{
		rgv.move(pCNC);
		rgv.load(pCNC);
		rgv.clean(pCNC);
	}
	cout << "��������������" << rgv.sum << endl;
	system("pause");
	return 0;
}
