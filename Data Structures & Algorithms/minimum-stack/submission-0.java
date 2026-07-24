class MinStack {

    public ArrayList<Integer> stack;
    public int size;

    public MinStack() {
        stack = new ArrayList<>();
    }
    
    public void push(int val) {
        stack.add(val);
        size++;
    }
    
    public void pop() {
        stack.remove(size - 1);
        size--;
    }
    
    public int top() {
        return stack.get(size - 1);
    }
    
    public int getMin() {
        int min = 0;
        for (int i = 0; i < size; i++) {
            if (i == 0) {
                min = stack.get(i);
            } else if (min > stack.get(i)) {
                min = stack.get(i);
            }
        }
        return min;
    }
}
