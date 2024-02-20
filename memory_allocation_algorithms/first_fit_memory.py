memory = [100, 500, 200, 300, 600]
no_of_processes = 4
processes = []

for i in range(no_of_processes):
    processes.append(int(input(f"Enter the process's size of {i+1}: ")))

ascending_memory = sorted(memory)
print(processes)
print(ascending_memory)

def first_fit(memory,processes):
    allocation={}
    for process in processes:
        for i, m in enumerate(memory):
            if m >=process:
                allocation[process] = m
                memory[i] -= process
                break
    return allocation

first_fit_allocation = first_fit(memory.copy(), processes)


print("First Fit Allocation:")
print(first_fit_allocation)


print("Efficient Utilization:")
print("First Fit Memory Utilization: ", sum(memory) - sum(first_fit_allocation.values()))