#include <iostream>
#include <vector>
#include <random>


using namespace std;

void selection_sort(vector<double> & X){
	
	int n = X.size();
	int lowest_idx;
	double smallest_value, current_first;
	
	for (int i = 0; i < n; i++){		
		lowest_idx = i;		
		for (int j = i+1; j < n; j++){
		     if (X[j] < X[lowest_idx]){
		     	  lowest_idx = j;
			 }
	    }			
		smallest_value = X[lowest_idx];
		current_first = X[i];
		X[i] = smallest_value;
		X[lowest_idx] = current_first;
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
  
  selection_sort(X);
  
  cout << "The random vector has been sorted in ascending order: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
	cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
  
}
