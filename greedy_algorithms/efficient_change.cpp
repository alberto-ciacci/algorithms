#include <iostream>
#include <vector>
#include <math.h> 
#include <iomanip>
#include <stdlib.h>

using namespace std;

double efficient_change(double change, vector<double>&denominations, vector<int>&quantities, vector<int>&paid_back_quantities) {

  double paid_change = 0;
  int n = denominations.size();
  while(paid_change < change){
  	    double largest_denomination = 0;
  	    int largest_idx = 0;
  	    for (int i = 0; i < n; ++i){
  	    	 if((denominations[i] >= largest_denomination) & (denominations[i] + paid_change <= change) & (quantities[i] > 0)){
  	    	           largest_denomination = denominations[i];	
  	    	           largest_idx = i;
			  }
		}
		paid_change += largest_denomination;
		quantities[largest_idx] -= 1;
		paid_back_quantities[largest_idx] +=1;
  	    
  }
  return paid_change;
}

int main() {
  double paid_amount;
  double price;
  double change;
  int n;
  cout << "Input the amount that the client has paid (in multiple of 0.01$): ";
  cin >> paid_amount;
  cout << "Input the price of the requested service (in multiple of 0.01$): ";
  cin >> price;
  change = paid_amount - price;
  if (change < 0){
  	  cout << "The client has not paid the full price of the requested service. The program is now closing.";
  	  exit(1);
  }else if (change == 0){
  	  cout << "The client has paid the exact price of the requested service. The program is now closing.";
  	  exit(1);
  }else{
	  cout << "Input the number of different coin/banknote denominations that are available in the cash machine: ";
	  cin >> n;
	  vector<double> denominations(n);
	  vector<int> quantities(n);
	  vector<int> paid_back_quantities(n);
	  if (n > 0){
			  cout << "Input the denominations followed by the respective quantities (double + space + integer): " << "\n";
			  for (int i = 0; i < n; i++) {
			  	  cout << "Denomination and quantity #" << i + 1 << ": ";
			      cin >> denominations[i] >> quantities[i];
			      paid_back_quantities.push_back(0);
			  }
	  }
	  double paid_change = efficient_change(change, denominations, quantities, paid_back_quantities);
	  if (paid_change < change){
	  	  cout << "You were unable to pay the change. The program is now closing.";
	  	  exit(1);
	  }else{
	  	  cout << "The following table shows the most efficient way to pay " << change << "$ given the available coins and banknotes in the cash machine." << "\n";
	  	  cout << "denomination" << "\t" << "quantity" << "\n";
	  	  for (int i = n-1; i > - 1; i--){
	  	  	   if (paid_back_quantities[i] > 0){
	  	  	   		cout << denominations[i] << "\t" << paid_back_quantities[i] << "\n";
				}
		  }
	  }
   }
}
