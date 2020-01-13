/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | Copyright (C) 2013 OpenFOAM Foundation
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

\*---------------------------------------------------------------------------*/
#include "fvCFD.H"
#include "mathematicalConstants.H"
#include "demandDrivenData.H"
#include "meshSearch.H"
#include <math.h>
// * * * * * * * * * * * * * * Static Data Members * * * * * * * * * * * * * //

// * * * * * * * * * * * * * * main function  * * * * * * * * * * * * * * //

int main(int argc, char *argv[])
{
   
#   include "setRootCase.H"
#   include "createTime.H"
#   include "createMesh.H"
#   include <fstream>
#   include <iostream>
//	#define Umax  7.5
//	#define rIB  0.0016
	volScalarField solidfractionMean //读取时均固相分数场
    	(
       		IOobject
        	(
            	"solidfractionMean",
            	runTime.timeName(),
            	mesh,
            	IOobject::MUST_READ,
            	IOobject::AUTO_WRITE
        	),
        	mesh
    	);
	
	volScalarField pMean			//读取时均压力场
    	(
       		IOobject
        	(
            	"pMean",
            	runTime.timeName(),
            	mesh,
            	IOobject::MUST_READ,
            	IOobject::AUTO_WRITE
        	),
        	mesh
    	);

	volVectorField UsMean			//读取时均固相速度场
    	(
       		IOobject
        	(
            	"UsMean",
            	runTime.timeName(),
            	mesh,
            	IOobject::MUST_READ,
            	IOobject::AUTO_WRITE
        	),
        	mesh
    	);
	const pointField& points = mesh.points();//获取网格内所有点坐标
	scalar gridLength = Foam::pow(mesh.V()[0],1.0/3.0);//求解网格长度

        double dx=0.,dy=0.,dz=0.;
	double x0=0.,y0=0.,z0=0.;
	double x1=0.,y1=0.,z1=0.;
	char fileName[1024];
	

	// local boundary
	//求取网格顶点xyz方向上的边界
	forAll(points,i){
		double x = points[i].x();
		double y = points[i].y();
		double z = points[i].z();

		if (i==0) {
			x0 = x;
			y0 = y;
			z0 = z;
			x1 = x;
			y1 = y;
			z1 = z;
		} else {
			x0 = x0 < x ? x0 : x;
			y0 = y0 < y ? y0 : y;
			z0 = z0 < z ? z0 : z;
			x1 = x1 > x ? x1 : x;
			y1 = y1 > y ? y1 : y;
			z1 = z1 > z ? z1 : z;
		}
	}

	// cal the number of cell in x-y-z direction
	// only for uniform mesh
	//求取xyz方向上的网格数目
	label Nx = (int) (mag(x1-x0)/gridLength + 0.5);
	label Ny = (int) (mag(y1-y0)/gridLength + 0.5);
	label Nz = (int) (mag(z1-z0)/gridLength + 0.5);

	//创建数组用来存储轴向时均值的大小
	scalarField solidfractionOut(Nz,0.0);
	scalarField pOut(Nz,0.0);
	scalarField UszOut(Nz,0.0);
	scalarField sA(Nz,0.0);

	forAll(UsMean,cellI){//遍历所有网格内的值
		//cellI为网格的编号，而index为高度编号
		int index =  (int) (mesh.C()[cellI][2]/gridLength);
		scalar i_sA = mesh.V()[cellI]/gridLength;//求取网格xy平面面积s_xy
		solidfractionOut[index] += (solidfractionMean[cellI]*i_sA);//s_xy*场值大小		
		pOut[index] += (pMean[cellI]*i_sA);		
		UszOut[index] += (UsMean[cellI][2]*i_sA);		
		sA[index] += i_sA;//xy平面总截面积
	}
	solidfractionOut /= sA;	//求取截面平均
	pOut /= sA;	
	UszOut /= sA;	
	

	sprintf(fileName, "postprocessing.out");//输出到文件
	FILE *fout = fopen(fileName, "w");

	forAll(solidfractionOut,hi){
		scalar hValue = (hi+0.5)*gridLength;
		fprintf(fout, "%f\t %f\t %f\t %f\n",hValue,solidfractionOut[hi],pOut[hi],UszOut[hi]);//\t为制表符 \n为回车符
		//Info<< (hi+0.5)*gridLength <<", "<<solidfractionOut[hi]<< ", "<<pOut[hi]<<", "<<UszOut[hi]<<endl;
	}

	fclose(fout);

	return 0;
}





// ************************************************************************* //
