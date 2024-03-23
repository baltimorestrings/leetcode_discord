package textbook_work;

import javax.swing.*;
import java.util.Arrays;
import java.util.Objects;
import java.util.stream.Collectors;

@SuppressWarnings("unchecked")
class Ch1_List<T extends Comparable<T>> {

    /**
     * internal storage
     */
    private Object[] innerList;

    /**
     * default array size
     */
    private static final int defaultInitialSize = 10;

    /**
     * the effective length
     */
    private int numObjects = 0;

    private void throw_if_bad_index(int index) {
        if (index >= numObjects || index < 0) {
            throw new ArrayIndexOutOfBoundsException("Index out of bounds: " + index + " is not a valid index.");
        }
    }
    public Ch1_List(int initialSize) {
        innerList = new Object[initialSize];
    }

    public Ch1_List() {
        this(defaultInitialSize);
    }

    public T get(int index) {
        throw_if_bad_index(index);
        return (T) innerList[index];
    }

    public void set(int index, T object) {
        throw_if_bad_index(index);
        innerList[index] = object;
    }

    public void append(T object) {
        if (numObjects == innerList.length) {
            grow();
        }
        innerList[numObjects] = object;
        numObjects++;
    }

    public void insert(int index, T object) {
        throw_if_bad_index(index);
        if (innerList.length + 1 >= innerList.length) {
            grow();
        }
        for(int i = numObjects; i > index; i--) {
            innerList[i] = innerList[i - 1];
        }
        innerList[index] = object;
    }
    
    private void grow() {
        innerList = Arrays.copyOf(innerList, innerList.length * 2);
    }

    public int size() {
        return numObjects;
    }

    public String toString() {
        return "SimpleList[" + Arrays.stream(innerList).limit(numObjects).map(Objects::toString).collect(Collectors.joining(", ")) + "]";
    }

    public static void main(String[] args) {
        Ch1_List c = new Ch1_List<Integer>(10);
        c.append(1);
        c.append(3);
        c.append(5);
        System.out.println(c);
    }
}