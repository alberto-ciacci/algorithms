#include <iostream>
#include <stdlib.h>  
#include <vector>
#include <math.h>
#include <ctime>
using namespace std;

void merge(vector<int> &X, int a, int n, int b){
	
	int n1 = n - a + 1;
	int n2 = b - n;
	vector<int> L1(n1 + 1);
	vector<int> L2(n2 + 1);
	for (int i = 0; i < n1; i++) {
		L1[i] = X[a + i];
    }
    
    for (int i = 0; i < n2; i++) {
		L2[i] = X[n + i + 1];
    }
    
    L1[n1] = INT_MAX;
    L2[n2] = INT_MAX;
    
    int counter1 = 0;
    int counter2 = 0;
    
    for (int i = a; i < b + 1; i++) {
		if (L1[counter1] <= L2[counter2] ){
			X[i] = L1[counter1];
			counter1 +=1;
		}else{
            X[i] = L2[counter2];
			counter2 +=1;			
		}
    }
    
    
	
}

void merge_sort(vector<int> &X, int a, int b){
	if (a < b){
		int n = 0.5*(a + b);
		merge_sort(X, a, n);
		merge_sort(X, n + 1, b);
		merge(X,a,n,b);		
	}
}


int main() {
	
  int low, high, n, k;
  
  cout << "Input the size of the random and uniformly distributed vector (integer) that we are about to create: "; cin >> n ;
  cout << "Input the lower bound of the uniform distribution: "; cin >> low;
  cout << "Input the upper bound of the uniform distribution: "; cin >> high;
  
  vector<int> X(n);
  srand((unsigned int)time(NULL));
  
  for (int i = 0; i < n; i++) {
		X[i] = rand() % high + low; 
  }	
  
  merge_sort(X, 0, X.size() - 1);
  
  cout << "\n" << "The random vector has been sorted in ascending order: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
		cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
  
}
