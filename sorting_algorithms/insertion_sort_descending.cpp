#include <iostream>
#include <vector>
#include <random>
#include <limits>


using namespace std;

void insertion_sort_descending(vector<double> &X){
	int n = X.size();
	int j;
	double key;
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
  
  insertion_sort_descending(X);
  
  cout << "\n" << "The random vector has been sorted in ascending order: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
	cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
  
}
