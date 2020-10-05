#include <iostream>
#include<string>  

using namespace std;

int main()
{
    long long subjects;
    long long standing;
    int round = 0;
    long long subjectsInput;

    cout << "Number of subjects in the simulation (default:100000000): ";
    cin >> subjectsInput;
    cout << "\n";

    subjects = subjectsInput;

    if (!subjects) 
    { 
        cout << "Invalid Input! Using default number of subjects. \n" << endl;
        subjects = 100000000; 
    }

    cout << "Starting with " + to_string(subjects) +  " subjects\n" << endl;

    while (subjects > 1)
    {
        standing = 0;
        round++;
        for (int i = 0; i < subjects; i++)
        {
            if (rand() % 2)
            { standing++; }
        }

        cout << "Out of " + to_string(subjects) + "; " + to_string(standing) + " flipped heads " + to_string(round) + " time/s" << endl;
        cout << "Percentage Passed: " + to_string(((float)standing / (float)subjects) * 100) + " %\n"<< endl;
        subjects = standing;
    }

    if (subjects == 1)
    {
    cout << "In this simulation " + to_string(subjects) + " person flipped heads " + to_string(round) + " times\n" << endl;
    }
    
    // cout << "Press Enter To Exit..." << endl;
    // cin.ignore();
    return 0;
}