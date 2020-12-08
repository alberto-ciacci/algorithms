#include <iostream>
#include <stdlib.h>  
#include <vector>
#include <math.h>
#include <ctime>
using namespace std;
using std::swap;

void selection_sort(vector<int> & X){
	
	int n = X.size();
	int lowest_idx;
	
	for (int i = 0; i < n; i++){		
		lowest_idx = i;		
		for (int j = i+1; j < n; j++){
		     if (X[j] < X[lowest_idx]){
		     	  lowest_idx = j;
			 }
	    }
		swap(X[lowest_idx],X[i]);			
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
  
  selection_sort(X);
  
  cout << "\n" << "The random vector has been sorted in ascending order: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
		cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
  
}
