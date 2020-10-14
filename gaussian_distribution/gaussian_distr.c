/*************************************************************************
      > File Name: gaussian_distr.c
      > Author: zhaopeng
      > Mail: zhaopeng_chem@163.com
      > Created doubleime: Wed 14 Oct 2020 08:37:19 AM CSdouble
      > Box–Muller transform method (https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform)
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define M_PI 3.14159265358979323846

double generateGaussianNoise(double mu, double sigma){
	double twopi = 2.0 * M_PI;
	double r_a = rand()/(RAND_MAX + 1.0);
	double r_b = rand()/(RAND_MAX + 1.0);
	double u1 = 1.0f - r_a;// [0, 1) -> (0, 1]
	double u2 = r_b;
	double radius = sqrt(-2.0 * log(u1));
	double theta = twopi * u2;
	double data = radius * cos(theta);
	return data * sigma + mu;
}

double generateLogNormalNoise(double mu, double sigma){
	double twopi = 2.0 * M_PI;
	double r_a = rand()/(RAND_MAX + 1.0);
	double r_b = rand()/(RAND_MAX + 1.0);
	double u1 = 1.0f - r_a;// [0, 1) -> (0, 1]
	double u2 = r_b;
	double radius = sqrt(-2.0 * log(u1));
	double theta = twopi * u2;
	double data = radius * cos(theta);
	return exp(data * sigma + mu);
}

int main(){

	int count = 200000;
	double mu = 0.0;
	double sigma = 0.5;
	for (int i = 0; i<count; i++){
		//double ret = generateGaussianNoise(mu, sigma);
		double ret = generateLogNormalNoise(mu, sigma);
		printf("%lf\n", ret);
	}
	return 0;
}
