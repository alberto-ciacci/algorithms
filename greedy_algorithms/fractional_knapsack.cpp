#include <iostream>
#include <vector>
#include <stdint.h>
#include <inttypes.h>
#include <math.h> 
#include <iomanip>

using namespace std;

int fractional_knapsack(int capacity, vector<int>&weights, vector<int>&values){
	// retrieve the number of different objects that can be included in the knapsack
	int n = weights.size();
	// track the value of the objects that have been included in the knapsack
	double added_value = 0.0;
	// loop over the objects
	for(int i = 0; i < n; ++i){
		// terminate the algorithm if there is no capacity left (i.e., knapsack is full)
		if (capacity == 0){
			// return the value of the objects that have been included in the knapsack
			return added_value;
		}
		// determine the current optimal choice
		double optimal_choice = 0.0;
		int optimal_choice_idx = 0;
		for(int j = 0; j < n; ++j){
			if((values[j]/ (double) weights[j] > optimal_choice) & (weights[j] > 0)){
				optimal_choice = values[j]/ (double) weights[j];
				optimal_choice_idx = j;
			}
	    }
        // add the optimal choice to the knapsack and update the weights and current capacity
	    double current_pick = min(weights[optimal_choice_idx], capacity);
	    added_value += current_pick*optimal_choice;
	    weights[optimal_choice_idx] -= current_pick;
	    capacity -= current_pick;		
	}
	// return the value of the objects that have been included in the knapsack
	return added_value;
}

int main() {
  int n;
  int capacity;
  cout << "Input the number of different objects that can be added to the knapsack (integer): ";
  cin >> n ;
  cout << "Input the capacity of the knapsack (integer): ";
  cin >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  cout << "Input the value and weight of each object that can be added to the knapsack (integer + space + integer): " << "\n";
  for (int i = 0; i < n; i++) {
      cin >> values[i] >> weights[i];
  }

  double value_in_knapsack = fractional_knapsack(capacity, weights, values);

  cout << "The maximum attainable value that can be added to the knapsack is: ";
  cout << std::setprecision(10) << value_in_knapsack << endl;
  return 0;
}
	
