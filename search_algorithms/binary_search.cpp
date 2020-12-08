#include <iostream>
#include <stdlib.h>  
#include <vector>
#include <math.h>
#include <ctime>

using namespace std;

int binary_search(const vector<int> &X, int left, int right, int k) {

  if (right <= left){
  	  return -1;
  }
  
  int mid = floor(0.5*(left + right));
  
  if (k == X[mid]){
  	  return mid;
  }else if (k < X[mid]){
  	  return binary_search(X, left, mid,k);
  }else{
  	  return binary_search(X, mid + 1, right,k); 
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
  
  cout << "Guess an integer: "; cin >> k;
  int output = binary_search(X, 0, X.size(), k);
  if (output == -1){
  	   cout << "The number " << k << " is not an element of the random vector. Try again!" << "\n";
  }else{
  	   cout << "Your guess is correct! The number " << k << " is an element of the random vector." << "\n";
  }
  
  cout <<  "Here the random vector: " << "\n" << "\n";
  for (int i = 0; i < n; i++) {
		cout << "#" << i+1 << "\t" << X[i] << "\n";
  }
}
