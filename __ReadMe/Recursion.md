How will you explain Recursion to a 4 year old?
	Russian Dolls
Combinatorial Problems Mental Model
	Helpful Visualization tool


void helper(    vector<int>& A,
                vector<int>& subset,
                int index)
{
    print_subset(subset);       // print the subset
    for (int i = index; i < A.size(); i++) {
        // make choice
        subset.push_back(A[i]);

        helper(A, res, subset, i + 1);

        // unmake choice
        subset.pop_back();
    }
    return;
}
