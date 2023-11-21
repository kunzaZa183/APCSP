mat = [[5,7,9,2,1,9],
       [5,3,4,0,0],
       [3,7,0,8,9],
       [0,0,]]

for row in mat :
    for item in row :
        print( item , end=" " )

# Finding the average of each row
for i, row in enumerate(mat):
    row_sum = sum(row)
    row_avg = row_sum / len(row)
    print(f"Average of elements in row {i+1}: {row_avg}")

# Transposing the matrix
transposed_mat = []
for i in range(len(mat[0])):
    transposed_row = []
    for row in mat:
        if i < len(row):
            transposed_row.append(row[i])
    transposed_mat.append(transposed_row)

print("Transposed matrix:")
for row in transposed_mat:
    print(*row)


# Multiplying each element by a scalar (e.g., 2)
scalar = 2
result_matrix = [[element * scalar for element in row] for row in mat]
print("Matrix multiplied by", scalar, ":")
for row in result_matrix:
    print(*row)
