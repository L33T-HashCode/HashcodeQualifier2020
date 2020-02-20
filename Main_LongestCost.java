import java.awt.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        String[] inputs = new String[]{"a_example.txt", "b_read_on.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt", "c_incunabula.txt",};
        for (String inputStr : inputs) {
            File input = new File(inputStr);
            Scanner reader = new Scanner(input);
            String temp = reader.nextLine();
            String[] tempArr = temp.split(" ");
            int numBooks = Integer.parseInt(tempArr[0]);
            int numLib = Integer.parseInt(tempArr[1]);
            int numDays = Integer.parseInt(tempArr[0]);
            ArrayList<Book> worldCollection = new ArrayList<>();
            ArrayList<Library> worldLibs = new ArrayList<>();
            ArrayList<Library> markedWorldLibs = new ArrayList<>();
            HashSet<Integer> set = new HashSet<>();

            temp = reader.nextLine();
            tempArr = temp.split(" ");
            for (int i = 0; i < tempArr.length; i++) {
                worldCollection.add(new Book(i, Integer.parseInt(tempArr[i])));
            }
            for (int i = 0; i < numLib; i++) {
                temp = reader.nextLine();
                tempArr = temp.split(" ");
                int libNumDays = Integer.parseInt(tempArr[1]);
                int bookPerDay = Integer.parseInt(tempArr[2]);
                ArrayList<Book> collection = new ArrayList<>();
                temp = reader.nextLine();
                tempArr = temp.split(" ");
                for (String s : tempArr) {
                    collection.add(worldCollection.get(Integer.parseInt(s)));
                }
                Collections.sort(collection);
                worldLibs.add(new Library(i, libNumDays, collection, bookPerDay));
            }
            reader.close();
            Collections.sort(worldLibs);
            for (int dayCount = 0; dayCount <= numDays; dayCount++) {
                if (worldLibs.size() > 0) {
                    Library curr = worldLibs.get(0);
                    if (curr.signUpCost > 0) {
                        curr.signUpCost--;
                    } else {
                        markedWorldLibs.add(curr);
                        worldLibs.remove(curr);
                    }
                }
                for (Library l : markedWorldLibs) {
                    for (int i = 0; i < l.booksPerDay; i++) {
                        Book b = l.getMaxBook(set);
                        if (b != null) {
                            set.add(b.bId);
                            worldCollection.remove(b);
                        }
                    }
                }
            }
            File out = new File(inputStr.charAt(0) + "_out.txt");
            FileWriter writer = new FileWriter(out);
            String result = markedWorldLibs.size() + "\n";
            for (Library l : markedWorldLibs) {
                result += (l.lId + " " + l.scannedIdx.size() +"\n");
                for (int i : l.scannedIdx) {
                    result += (i + " ");
                }
                result += ("\n");
            }
            writer.write(result);
            writer.close();
            System.out.println("Finished " + inputStr.charAt(0));
        }
    }
}

class Book implements Comparable{
    int bId;
    int score;

    public Book(int id, int score) {
        this.bId = id;
        this.score = score;
    }


    @Override
    public int compareTo(Object o) {
        Book book = (Book) o;
        return Integer.compare(this.score, book.score);
    }
}

class Library implements Comparable {
    int lId;
    int signUpCost;
    int booksPerDay;
    int score = 0;
    ArrayList<Book> books;
    HashSet<Integer> scannedIdx = new HashSet<>();

    public Library(int lId, int signUp, ArrayList<Book> books, int booksPerDay) {
        this.lId = lId;
        this.signUpCost = signUp;
        this.books = books;
        this.booksPerDay = booksPerDay;
        for (Book b : books) {
            score += b.score;
        }
    }

    public Book getMaxBook(HashSet<Integer> set) {
        Book temp = null;
        for (Book b : books) {
            if (!set.contains(b.bId)) {
                books.remove(b);
                scannedIdx.add(b.bId);
                return b;
            } else {
                temp = b;
            }
        }
        if (temp != null) {
            books.remove(temp);
            scannedIdx.add(temp.bId);
        }
        return temp;
    }

    @Override
    public int compareTo(Object o) {
        Library lib = (Library) o;
        return Integer.compare(this.signUpCost, lib.signUpCost);
    }
}
