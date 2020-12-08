#include <iostream>
#include <stdlib.h>  
#include <vector>
#include <math.h>
#include <ctime>


using namespace std;

void insertion_sort_descending(vector<int> &X){
	int n = X.size();
	int j;
	int key;
	for (int i = 1; i < n; i++){
		key = X[i];
		j = i - 1;
		while((j > - 1) & (X[j] < key)){
			X[j + 1] = X[j];
			j -= 1;
		}
		X[j + 1] = key;		
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
  
  insertion_sort_descending(X);
  
  cout << "\n" << "The random vector has been sorted in descending order: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
		cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
  
}
