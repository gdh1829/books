# Fundamentals

first citizen
second citizen
method reference ::

## predicate
is often used in mathmatics to mean something function-like that takes a value for an argument and returns _true_ or _false_.

## Collection Functions
static <T> Collection<T> filter(Collection<T> c, Predicate<T> p);

## External iteration(by Collections API) vs Internal iteration(by Streams API)
```java
Map<Currency, List<Transaction>> transactionsByCurrencies = new HashMap<>();
for (Transaction transaction : transactions) { // Loop
    if(transaction.getPrice() > 1000) { // filter expensive transactions
        Currency currency = transaction.getCurrency();
        List<Transaction> transactionsForCurrency = transactionsByCurrencies.get(currency);
        // grouping
        if (transactionsForCurrency == null) {
            transactionsForCurrency = new ArrayList<>();
            transactionsByCurrencies.put(currency, transactionsForCurrency);
        }
        transactionsForCurrency.add(transaction);
    }
}
```

```java
import static java.util.stream.Collectors.groupingBy;
Map<Currency, List<Transaction>> transactionsByCurrencies = transactions.stream()
    .filter((Transaction) t -> t.getPrice() > 1000) // filter expensive transactions
    .collect(groupingBy(Transaction::getCurrency)); // group them by currency
```

## Pain points of working with Collections API in comparison to Streams API
1. Using collections, you're managing iteration process yourself.
    - You needa to iterate through the elements one by one using a _for-each_ loop processing them in turn.
    - In contrast, using Streams API, you don't need to think in terms of loops. The data processing happens internally inside the library. We called this _internal iteration_
1. When you have a vast amounts of transactions, a single CPU wouldn't be able to process this large amount of data.
    - Many new laptop and desktop computers are recently and generally provided with multicores.
    - In theory, if you have eight cores, they should be able to process your data eight times as fast as using one core, because they work in parallel.

## Java 8 addresses both problems (boilerplate and obscurity involving processing collections and difficulty exploiting multicore) with the Streams API (java.util.stream)
The first design motivator is that there are many data-processing patterns that occur over and over again and the would benefit from forming part of a library: _filtering_ data based on a criterion, _extracting_ data, or _grouping_ data, and so on.
The second motivator is that such operations can often be parallelized.
For now, we'll just say that the new Streams API behaves similarly to Java's existing Collections API: both provide access to sequences of data items. But it's useful for now to keep in mind that Collections is mostly about storing and accessing data, whereas Streams is mostly about describing computations on data. The key point here is that the Streams API allows and encourages the elements within a stream to be processed in parallel.

```java
import static java.util.stream.Collectors.groupingBy;
Map<Currency, List<Transaction>> transactionsByCurrencies = transactions.parallelStream() // stream in parallel
    .filter((Transaction) t -> t.getPrice() > 1000) // filter expensive transactions
    .collect(groupingBy(Transaction::getCurrency)); // group them by currency
```

## Parallelism in Java and no shared mutable state
People have always said parallelism in Java is difficult, and all this stuff about _synchronized_ is error-prone. Where's the magic bullet in Java 8?
There are two magic bullets. First, the library handles partitioning - breaking down a big stream into several smaller streams to be processed in parallel for you. Second, this parallelism almost for free from streams, works only if the methods passed to library methods like _filter_ don't interact (ex, by having no mutable shared objects). But it turns out that this restriction feels natural to a coder. Although the primary meaning of _functional_ in _functional programming_ means "using functions as first-class values," it often has a secondary nuance of "no interaction during execution between components."

## default method that has implementation in interface class
Prior to Java 8, things like List<T> or Collections<T> doesn't have _stream_ or _parallelStream_ because these methods hadn't been conceived of. Adding a new method to an interface means all concrete classes must provide an implementation for it, this would've been a nightmare for users.
The Java 8 solution is to break the last link: an interface can now contain method signatures for which an implementing class doesn't provide an implementation. Then who implements them? The missing method bodies are given as part of the interface (hence default implementations) rather than in the implementing class. Java 8 allows the existing _default_ keyword to be used in interface specifications to achieve this.
For example, in Java 8, you can call the _sort_ method directly on a list. This is made possible with the following default method in the Java 8 _List_ interface, which calls the static method _Collections.sort_:

```java
default void sort (Comparator<? super E> c) {
    Collections.sort(this, c);
}
```

This means any concrete classes of _List_ don't have to explictily implement _sort_, whereas in previous Java verions such concrete classes would fail to recompile unless they provided an implementation for _sort_.

## Other good ideas from functional programming
Optional<T>
Java 8 introduced the _Optional<T>_ class that, if used consistently, can help you avoid null-pointer exceptions. It's a container object that may or may not contain a value. _Optional<T> includes methods to explicitly deal with the case where a value is absent, and as a result you can avoid null-pointer exceptions. It uses the type system to allow you to indicate when a variable is anticipated to potentially have a missing value.
Strunctural pattern mathching
This is used in mathematics. For example,

```
f(0) = 1
f(n) = n*f(n-1) otherwise
```
