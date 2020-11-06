#include <iostream>
#include <vector>
#include <random>
#include <limits>


using namespace std;

void bubble_sort(vector<double> &X){
	int n = X.size();
	double swap1, swap2;
	for (int i = 0; i < n - 1; i++){
		for (int j = n - 1; j > i; j--){
			if (X[j] < X[j-1]){
				swap1 = X[j];
				swap2 = X[j-1];
				X[j] = swap2;
				X[j-1] = swap1;
			}
        }  
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
  
  bubble_sort(X);
  
  cout << "\n" << "The random vector has been sorted in ascending order: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
	cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
  
}
