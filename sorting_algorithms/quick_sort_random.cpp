#include <iostream>
#include <stdlib.h>  
#include <vector>
#include <math.h>
#include <ctime>
using namespace std;
using std::swap;

int random_partition(vector<int> &X, int a, int b){
	
	int random_idx = rand() % (b-a) + a;
	swap(X[a],X[random_idx]);
		
    int pivot = X[a];
	int j = a;
	for(int i = a + 1; i <= b; i++){
		if(X[i] <= pivot){
		   j +=1;
           swap(X[j],X[i]);
		}
	}
    swap(X[a],X[j]);
	return j;
}

void random_quick_sort(vector<int> &X, int a, int b){
	if (a >= b){
		return;
	}
	int idx = random_partition(X, a, b);
	random_quick_sort(X, a, idx-1);
	random_quick_sort(X, idx+1, b);
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
  
  random_quick_sort(X, 0, X.size() - 1);
  
  cout << "\n" << "The random vector has been sorted in ascending order: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
		cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
  
}
