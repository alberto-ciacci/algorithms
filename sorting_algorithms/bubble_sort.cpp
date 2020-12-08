#include <iostream>
#include <stdlib.h>  
#include <vector>
#include <math.h>
#include <ctime>


using namespace std;
using std::swap;

void bubble_sort(vector<int> &X){
	int n = X.size();
	for (int i = 0; i < n - 1; i++){
		for (int j = n - 1; j > i; j--){
			if (X[j] < X[j-1]){
				swap(X[j], X[j-1]);
			}
        }  
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
  
  bubble_sort(X);
  
  cout << "\n" << "The random vector has been sorted in ascending order: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
		cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
  
}
