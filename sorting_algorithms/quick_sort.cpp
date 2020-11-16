#include <iostream>
#include <vector>
#include <random>
#include <limits>
#include <time.h> 

using std::swap;


using namespace std;

int partition(vector<double> &X, int a, int b){
	double pivot = X[a];
	int j = a;
	for(int i = a + 1; i < b; i++){
		if(X[i] < pivot){
		   j +=1;
		   swap(X[j],X[i]);
		}
	}
    swap(X[a],X[j]);
	return j;
}

void quicksort(vector<double> &X, int a, int b){
	if (a >= b){
		return;
	}
	int idx = partition(X, a, b);
	quicksort(X, a, idx-1);
	quicksort(X, idx+1, b);
}

int main() {
	
	
  double low;
  double high;
  int n;
  cout << "Input the size of the random and uniformly distributed vector that we are about to create: ";
  cin >> n ;
  cout << "Input the lower bound of the uniform distribution: ";
  cin >> low;
  cout << "Input the upper bound of the uniform distribution: ";
  cin >> high;
  vector<double> X(n);
  default_random_engine generator;
  std::uniform_real_distribution<double> dis(low,high);
  
  for (int i = 0; i < n; i++) {
        double rn = dis(generator);
		X[i] = rn;
  }
  
  cout << "\n";
  
  quicksort(X, 0, X.size());
  
  cout << "\n" << "The random vector has been sorted in ascending order: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
	cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
  
}
