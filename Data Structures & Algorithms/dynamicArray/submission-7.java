class DynamicArray {

    private int capacity = 0;
    private int size = 0;
    private Integer[] arrayList;
    public DynamicArray(int capacity) {
        this.arrayList = new Integer[capacity];
        this.capacity = capacity;
    }

    public int get(int i) {
        return (int) arrayList[i];
    }

    public void set(int i, int n) {
        if (arrayList[i] == null) {
            size++;
        }
        arrayList[i] = n;
    }

    public void pushback(int n) {
        if (size == capacity) {
            this.resize();
        }

        arrayList[size] = n;
        size++;

    }

    public int popback() {
        Integer hold = arrayList[size - 1];
        arrayList[size - 1] = null;
        size--;
        return (int) hold;
    }

    private void resize() {
        Integer[] newList = new Integer[this.capacity * 2];
        for (int i = 0; i < capacity; i++) {
            newList[i] = arrayList[i];
        }
        this.capacity *= 2;
        this.arrayList = newList;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
