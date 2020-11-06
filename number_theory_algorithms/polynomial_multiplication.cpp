#include <iostream>
#include <vector>
#include <stdint.h>
#include <inttypes.h>
#include <math.h>

using namespace std;

void polynomial_multiplication_naive(int degree, vector<double>&coeffs1, vector<double>&coeffs2, vector<double>&coeffs_final){
	      for (int i = 0; i <= degree-1; ++i){
	      		for (int j = 0; j <= degree-1; ++j){
	      	         coeffs_final[i + j] += coeffs1[i]*coeffs2[j];
		        } 	
		  }
}

void polynomial_multiplication_karatsuba(int degree, vector<double>&coeffs1, vector<double>&coeffs2, vector<double>&coeffs_final){
	      for (int i = 0; i <= degree-1; ++i){
	      		for (int j = 0; j <= degree-1; ++j){
	      	         coeffs_final[i + j] += coeffs1[i]*coeffs2[j];
		        } 	
		  }
}



int main(){
    vector <double> coeffs_final(2*degree - 1);
	
}
