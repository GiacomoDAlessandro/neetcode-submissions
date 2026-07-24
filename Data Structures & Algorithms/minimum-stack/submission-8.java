class MinStack {

    public ArrayList<Integer> stack;
    public int size;
    public Deque<Integer> minStack;

    public MinStack() {
        stack = new ArrayList<>();
        minStack = new ArrayDeque<>();
    }
    
    public void push(int val) {
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
        stack.add(val);
        size++;
    }
    
    public void pop() {
        if (stack.get(size - 1).equals(minStack.peek())) {
            minStack.pop();
        }
        stack.remove(size - 1);
        size--;
    }
    
    public int top() {
        return stack.get(size - 1);
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
