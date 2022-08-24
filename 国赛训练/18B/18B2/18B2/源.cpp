#include "stdafx.h"
#include "RGV.h"
#include "CNC.h"
#include <iterator>
#include <valarray>

#define CNC_NUMBER 8
#define TIME 28800
using namespace std;

int main( )
{
	int emu[254][8];  //枚举矩阵
	int i ;
	int j;
	for ( i = 1; i < 255; i++) {
		int n = i;
		for (j = 7; j >=0 ; j--){
			emu[i - 1][j] = (n==0) ? 0 :  n % 2;
			n = n / 2;
		}
	}

	int ans[254];   //结果向量

	for (int i = 0; i < 254; i++) {
		cout << i+1 << endl;
		RGV rgv=RGV() ;

		CNC cnc[CNC_NUMBER] = {
			CNC(1,0,emu[i][0]+1), CNC(2,0,emu[i][1] + 1), CNC(3,1,emu[i][2] + 1), CNC(4,1,emu[i][3] + 1),
			CNC(5,2,emu[i][4] + 1), CNC(6,2,emu[i][5] + 1), CNC(7,3,emu[i][6] + 1), CNC(8,3,emu[i][7] + 1) };
		CNC* pCNC = cnc;

		cout << "时间" << '\t' << "工序" << '\t' << "下料开始" << '\t' << "上料开始" << '\t' << "CNC#" << endl;

		rgv.Init(pCNC);

		while (rgv.time <= TIME)
		{
			rgv.move(pCNC);
			rgv.load(pCNC);
		}
		cout << "生成熟料总数：" << rgv.sum << endl<<endl;

		ans[i] = rgv.sum;

	}

	int max = 0;
	int index = 0;
	for (int i = 0; i < 254; i++) {
		if (ans[i]>max)
		{
			index = i + 1;
			max = ans[i];
		}
	}
	cout << index << " " << max;

	system("pause");
	return 0;
}
