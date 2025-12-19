# Complete TypeScript Cheat Sheet

## Table of Contents

### Part 1: TypeScript Foundations
- [1.1 Why TypeScript Exists](#11-why-typescript-exists)
- [1.2 TypeScript vs JavaScript](#12-typescript-vs-javascript)
- [1.3 Compile Time vs Runtime](#13-compile-time-vs-runtime)
- [1.4 Type Inference](#14-type-inference)
- [1.5 Type Annotations](#15-type-annotations)

### Part 2: Primitive & Special Types
- [2.1 Primitive Types](#21-primitive-types)
- [2.2 Any Type](#22-any-type)
- [2.3 Unknown Type](#23-unknown-type)
- [2.4 Never Type](#24-never-type)
- [2.5 Void Type](#25-void-type)

### Part 3: Variables & Functions
- [3.1 Typed Variables](#31-typed-variables)
- [3.2 Function Parameter Types](#32-function-parameter-types)
- [3.3 Function Return Types](#33-function-return-types)
- [3.4 Optional Parameters](#34-optional-parameters)
- [3.5 Default Parameters](#35-default-parameters)
- [3.6 Function Overloading](#36-function-overloading)

### Part 4: Arrays, Tuples & Enums
- [4.1 Typed Arrays](#41-typed-arrays)
- [4.2 Readonly Arrays](#42-readonly-arrays)
- [4.3 Tuples](#43-tuples)
- [4.4 Numeric Enums](#44-numeric-enums)
- [4.5 String Enums](#45-string-enums)
- [4.6 Enum Alternatives](#46-enum-alternatives)

### Part 5: Objects & Type Aliases
- [5.1 Object Typing](#51-object-typing)
- [5.2 Optional Properties](#52-optional-properties)
- [5.3 Readonly Properties](#53-readonly-properties)
- [5.4 Type Keyword](#54-type-keyword)
- [5.5 Nested Object Types](#55-nested-object-types)

### Part 6: Interfaces
- [6.1 Interface Syntax](#61-interface-syntax)
- [6.2 Interface vs Type](#62-interface-vs-type)
- [6.3 Extending Interfaces](#63-extending-interfaces)
- [6.4 Function Interfaces](#64-function-interfaces)
- [6.5 Index Signatures](#65-index-signatures)
- [6.6 Interfaces for APIs & DTOs](#66-interfaces-for-apis--dtos)

### Part 7: Union & Intersection Types
- [7.1 Union Types](#71-union-types)
- [7.2 Intersection Types](#72-intersection-types)
- [7.3 Discriminated Unions](#73-discriminated-unions)

### Part 8: Type Narrowing
- [8.1 Typeof Narrowing](#81-typeof-narrowing)
- [8.2 Instanceof Narrowing](#82-instanceof-narrowing)
- [8.3 In Operator](#83-in-operator)
- [8.4 Custom Type Guards](#84-custom-type-guards)

### Part 9: Generics
- [9.1 Generic Functions](#91-generic-functions)
- [9.2 Generic Interfaces](#92-generic-interfaces)
- [9.3 Generic Classes](#93-generic-classes)
- [9.4 Generic Constraints](#94-generic-constraints)

### Part 10: Utility Types
- [10.1 Partial](#101-partial)
- [10.2 Required](#102-required)
- [10.3 Pick](#103-pick)
- [10.4 Omit](#104-omit)
- [10.5 Readonly](#105-readonly)
- [10.6 Record](#106-record)
- [10.7 ReturnType](#107-returntype)
- [10.8 Parameters](#108-parameters)

### Part 11: Advanced Type System
- [11.1 Keyof Operator](#111-keyof-operator)
- [11.2 Indexed Access Types](#112-indexed-access-types)
- [11.3 Mapped Types](#113-mapped-types)
- [11.4 Conditional Types](#114-conditional-types)

### Part 12: Classes
- [12.1 Basic Class Syntax](#121-basic-class-syntax)
- [12.2 Typed Class Properties](#122-typed-class-properties)
- [12.3 Constructors with Types](#123-constructors-with-types)
- [12.4 Parameter Properties](#124-parameter-properties)
- [12.5 Method Typing](#125-method-typing)

### Part 13: Access Modifiers
- [13.1 Public](#131-public)
- [13.2 Private](#132-private)
- [13.3 Protected](#133-protected)
- [13.4 Readonly](#134-readonly)

### Part 14: Abstract Classes
- [14.1 Abstract Class Syntax](#141-abstract-class-syntax)
- [14.2 Abstract Methods](#142-abstract-methods)
- [14.3 Abstract Properties](#143-abstract-properties)
- [14.4 Abstract vs Interface](#144-abstract-vs-interface)

### Part 15: Static Members
- [15.1 Static Methods](#151-static-methods)
- [15.2 Static Properties](#152-static-properties)
- [15.3 Utility Patterns](#153-utility-patterns)

### Part 16: Async & Promises
- [16.1 Promise Types](#161-promise-types)
- [16.2 Async Function Typing](#162-async-function-typing)
- [16.3 Error Handling Types](#163-error-handling-types)
- [16.4 Result Type Pattern](#164-result-type-pattern)

### Part 17: TypeScript with Node.js
- [17.1 tsconfig Basics](#171-tsconfig-basics)
- [17.2 Strict Mode Flags](#172-strict-mode-flags)
- [17.3 ts-node](#173-ts-node)
- [17.4 Project Structure](#174-project-structure)
- [17.5 Build Process](#175-build-process)

### Part 18: Express & HTTP APIs
- [18.1 Request & Response Types](#181-request--response-types)
- [18.2 Middleware Typing](#182-middleware-typing)
- [18.3 Custom Request Interfaces](#183-custom-request-interfaces)

### Part 19: Environment Variables
- [19.1 Typing Environment Variables](#191-typing-environment-variables)
- [19.2 Safe Config Patterns](#192-safe-config-patterns)

### Part 20: DTOs & Validation
- [20.1 DTO Pattern](#201-dto-pattern)
- [20.2 Class-Based DTOs](#202-class-based-dtos)
- [20.3 Validation & Transformation](#203-validation--transformation)

### Part 21: Dependency Injection
- [21.1 Constructor Injection](#211-constructor-injection)
- [21.2 Provider Typing](#212-provider-typing)
- [21.3 Interface-Based Design](#213-interface-based-design)

### Part 22: Decorators
- [22.1 What Decorators Are](#221-what-decorators-are)
- [22.2 Framework Usage](#222-framework-usage)
- [22.3 Metadata Reflection](#223-metadata-reflection)

### Part 23: Backend Architecture
- [23.1 Service Layer Typing](#231-service-layer-typing)
- [23.2 Repository Pattern](#232-repository-pattern)
- [23.3 Clean Architecture](#233-clean-architecture)

### Part 24: Error Handling
- [24.1 Custom Error Classes](#241-custom-error-classes)
- [24.2 Typed Error Responses](#242-typed-error-responses)

### Part 25: Best Practices
- [25.1 Strict Mode Configuration](#251-strict-mode-configuration)
- [25.2 Common Mistakes](#252-common-mistakes)

### Part 26: Performance & Build
- [26.1 Compilation Speed](#261-compilation-speed)
- [26.2 Output Optimization](#262-output-optimization)
- [26.3 Build Configuration](#263-build-configuration)

---

## Part 1: TypeScript Foundations

### 1.1 Why TypeScript Exists

**Definition:** TypeScript is a superset of JavaScript that adds static typing to catch errors at compile time, improve code quality, and enhance IDE support.

**Benefits:**
- Catch errors before runtime
- Better IDE autocomplete and IntelliSense
- Improved code documentation
- Easier refactoring
- Better team collaboration

### 1.2 TypeScript vs JavaScript

| Feature | JavaScript | TypeScript |
|---------|-----------|------------|
| Typing | Dynamic | Static |
| Error Detection | Runtime | Compile time |
| Type Safety | No | Yes |
| IDE Support | Basic | Advanced |
| Learning Curve | Lower | Higher |

### 1.3 Compile Time vs Runtime

**Compile Time:** The phase where TypeScript code is checked for type errors and transpiled to JavaScript.

**Runtime:** The phase where JavaScript code executes in the browser or Node.js.

```typescript
// Compile time check
let x: number = 10;
x = "hello"; // Error at compile time

// Runtime execution
console.log(x); // This runs in JavaScript
```

### 1.4 Type Inference

**Definition:** TypeScript automatically infers types when you don't explicitly annotate them.

```typescript
let count = 5; // inferred as number
let message = "Hello"; // inferred as string
let isActive = true; // inferred as boolean

// Arrays
let numbers = [1, 2, 3]; // inferred as number[]

// Objects
let user = {
  name: "Alice",
  age: 30
}; // inferred as { name: string; age: number; }
```

### 1.5 Type Annotations

**Definition:** Explicitly declaring types for variables, parameters, and return values.

```typescript
// Variables
let username: string = "Alice";
let age: number = 30;
let isActive: boolean = true;

// Function parameters and return type
function greet(name: string): string {
  return `Hello, ${name}`;
}

// Arrays
let scores: number[] = [90, 85, 88];

// Objects
let user: { name: string; age: number } = {
  name: "Bob",
  age: 25
};
```

---

## Part 2: Primitive & Special Types

### 2.1 Primitive Types

**Definition:** Basic data types in TypeScript.

```typescript
// Number
let age: number = 30;
let price: number = 99.99;
let hex: number = 0xf00d;

// String
let name: string = "Alice";
let greeting: string = `Hello, ${name}`;

// Boolean
let isActive: boolean = true;
let hasPermission: boolean = false;

// Null
let empty: null = null;

// Undefined
let notAssigned: undefined = undefined;
```

### 2.2 Any Type

**Definition:** Disables type checking. Use sparingly as it defeats the purpose of TypeScript.

```typescript
let value: any = 10;
value = "text"; // OK
value = true; // OK
value.nonExistent(); // No error at compile time

// Avoid any when possible
// Bad
function process(data: any) {
  return data.value; // No type safety
}

// Good
function process(data: { value: string }) {
  return data.value; // Type safe
}
```

### 2.3 Unknown Type

**Definition:** A safer alternative to `any`. Requires type checking before use.

```typescript
let data: unknown;

data = 10;
data = "hello";
data = { name: "Alice" };

// Must narrow type before use
if (typeof data === "string") {
  console.log(data.toUpperCase()); // OK
}

// Type guard required
function processUnknown(value: unknown) {
  if (typeof value === "string") {
    return value.toUpperCase();
  }
  if (typeof value === "number") {
    return value.toFixed(2);
  }
  return "Unknown type";
}
```

### 2.4 Never Type

**Definition:** Represents values that never occur. Used for functions that never return.

```typescript
// Function that throws error
function throwError(message: string): never {
  throw new Error(message);
}

// Function with infinite loop
function infiniteLoop(): never {
  while (true) {
    // do something
  }
}

// Exhaustive type checking
type Status = "success" | "error";

function handleStatus(status: Status) {
  switch (status) {
    case "success":
      return "OK";
    case "error":
      return "Failed";
    default:
      const _exhaustive: never = status;
      return _exhaustive;
  }
}
```

### 2.5 Void Type

**Definition:** Indicates a function returns nothing (undefined).

```typescript
// Function with no return
function logMessage(message: string): void {
  console.log(message);
  // implicit return undefined
}

// Function with explicit return undefined
function clearCache(): void {
  cache.clear();
  return; // OK
}

// void vs undefined
function returnsVoid(): void {
  return; // OK
}

function returnsUndefined(): undefined {
  return undefined; // Must explicitly return undefined
}
```

---

## Part 3: Variables & Functions

### 3.1 Typed Variables

**Definition:** Variables with explicit type annotations.

```typescript
// Basic types
let age: number = 25;
let name: string = "Alice";
let isStudent: boolean = true;

// Multiple variables
let x: number, y: number, z: number;
x = 1;
y = 2;
z = 3;

// Const with types
const PI: number = 3.14159;
const API_URL: string = "https://api.example.com";
```

### 3.2 Function Parameter Types

**Definition:** Specifying types for function parameters.

```typescript
// Basic parameter types
function add(a: number, b: number) {
  return a + b;
}

// Multiple parameter types
function greet(name: string, age: number) {
  return `Hello ${name}, you are ${age} years old`;
}

// Object parameter
function printUser(user: { name: string; email: string }) {
  console.log(`${user.name}: ${user.email}`);
}

// Array parameter
function sum(numbers: number[]) {
  return numbers.reduce((acc, num) => acc + num, 0);
}
```

### 3.3 Function Return Types

**Definition:** Explicitly declaring what a function returns.

```typescript
// Explicit return type
function multiply(a: number, b: number): number {
  return a * b;
}

// String return type
function formatName(first: string, last: string): string {
  return `${first} ${last}`;
}

// Boolean return type
function isAdult(age: number): boolean {
  return age >= 18;
}

// Object return type
function createUser(name: string): { name: string; id: number } {
  return { name, id: Math.random() };
}

// Array return type
function getScores(): number[] {
  return [90, 85, 88];
}
```

### 3.4 Optional Parameters

**Definition:** Parameters that may or may not be provided.

```typescript
// Optional parameter with ?
function greet(name?: string) {
  return name ? `Hello ${name}` : "Hello";
}

greet(); // "Hello"
greet("Alice"); // "Hello Alice"

// Multiple optional parameters
function createUser(name: string, age?: number, email?: string) {
  return { name, age, email };
}

// Optional parameters must come after required ones
// This is wrong:
// function wrong(optional?: string, required: number) {} // Error

// Handling optional parameters
function buildUrl(base: string, path?: string) {
  return path ? `${base}/${path}` : base;
}
```

### 3.5 Default Parameters

**Definition:** Parameters with default values if not provided.

```typescript
// Default parameter
function greet(name: string = "Guest") {
  return `Hello ${name}`;
}

greet(); // "Hello Guest"
greet("Alice"); // "Hello Alice"

// Multiple default parameters
function createPoint(x: number = 0, y: number = 0) {
  return { x, y };
}

// Default with type inference
function multiply(a: number, b: number = 1) {
  return a * b;
}

// Default object parameter
function fetchData(url: string, options: { method: string } = { method: "GET" }) {
  // fetch logic
}
```

### 3.6 Function Overloading

**Definition:** Defining multiple function signatures for the same function name.

```typescript
// Overload signatures
function getValue(x: string): string;
function getValue(x: number): number;
function getValue(x: boolean): boolean;

// Implementation signature
function getValue(x: string | number | boolean): string | number | boolean {
  return x;
}

// Usage
let str = getValue("hello"); // string
let num = getValue(42); // number
let bool = getValue(true); // boolean

// More complex example
function makeDate(timestamp: number): Date;
function makeDate(year: number, month: number, day: number): Date;
function makeDate(yearOrTimestamp: number, month?: number, day?: number): Date {
  if (month !== undefined && day !== undefined) {
    return new Date(yearOrTimestamp, month, day);
  }
  return new Date(yearOrTimestamp);
}

// Arrow function with overloading
interface ProcessFn {
  (x: string): string;
  (x: number): number;
}

const process: ProcessFn = (x: any) => x;
```

---

## Part 4: Arrays, Tuples & Enums

### 4.1 Typed Arrays

**Definition:** Arrays with specific element types.

```typescript
// Number array
let numbers: number[] = [1, 2, 3, 4, 5];

// Alternative syntax
let scores: Array<number> = [90, 85, 88];

// String array
let names: string[] = ["Alice", "Bob", "Charlie"];

// Boolean array
let flags: boolean[] = [true, false, true];

// Mixed type array with union
let mixed: (string | number)[] = [1, "two", 3, "four"];

// Array of objects
let users: { name: string; age: number }[] = [
  { name: "Alice", age: 30 },
  { name: "Bob", age: 25 }
];

// Multi-dimensional arrays
let matrix: number[][] = [
  [1, 2, 3],
  [4, 5, 6]
];
```

### 4.2 Readonly Arrays

**Definition:** Arrays that cannot be modified after creation.

```typescript
// Readonly array
let ids: readonly number[] = [1, 2, 3];
// ids.push(4); // Error: Property 'push' does not exist

// Alternative syntax
let names: ReadonlyArray<string> = ["Alice", "Bob"];
// names[0] = "Charlie"; // Error: Index signature is readonly

// Use case: function parameters
function printValues(values: readonly string[]) {
  // values.push("new"); // Error
  console.log(values.join(", "));
}

// const assertions create readonly arrays
const colors = ["red", "green", "blue"] as const;
// colors[0] = "yellow"; // Error
```

### 4.3 Tuples

**Definition:** Fixed-length arrays with specific types for each position.

```typescript
// Basic tuple
let user: [number, string] = [1, "Alice"];

// Accessing tuple elements
let id = user[0]; // number
let name = user[1]; // string

// Tuple with multiple types
let response: [number, string, boolean] = [200, "OK", true];

// Optional tuple elements
let point: [number, number, number?] = [10, 20];
let point3D: [number, number, number?] = [10, 20, 30];

// Rest elements in tuples
let data: [string, ...number[]] = ["Alice", 1, 2, 3, 4];

// Readonly tuples
let coordinate: readonly [number, number] = [10, 20];
// coordinate[0] = 30; // Error

// Named tuple elements (TypeScript 4.0+)
type User = [id: number, name: string, active: boolean];
let user: User = [1, "Alice", true];

// Destructuring tuples
let [userId, userName] = user;
```

### 4.4 Numeric Enums

**Definition:** Named constants with numeric values.

```typescript
// Basic enum
enum Status {
  Pending,    // 0
  Active,     // 1
  Completed   // 2
}

let taskStatus: Status = Status.Active;

// Custom numeric values
enum HttpStatus {
  OK = 200,
  Created = 201,
  BadRequest = 400,
  NotFound = 404,
  ServerError = 500
}

// Auto-increment from custom value
enum Priority {
  Low = 1,    // 1
  Medium,     // 2
  High,       // 3
  Critical    // 4
}

// Reverse mapping
enum Direction {
  Up,
  Down,
  Left,
  Right
}

let dir = Direction.Up; // 0
let dirName = Direction[0]; // "Up"
```

### 4.5 String Enums

**Definition:** Enums with string values (no reverse mapping).

```typescript
// String enum
enum Role {
  Admin = "ADMIN",
  User = "USER",
  Guest = "GUEST",
  Moderator = "MODERATOR"
}

let userRole: Role = Role.Admin;

// Usage in functions
function checkPermission(role: Role) {
  if (role === Role.Admin) {
    return "Full access";
  }
  return "Limited access";
}

// Mixed enums (not recommended)
enum Mixed {
  No = 0,
  Yes = "YES"
}
```

### 4.6 Enum Alternatives

**Definition:** Using union types instead of enums (modern TypeScript preference).

```typescript
// Union type instead of enum
type Status = "pending" | "active" | "completed";

let taskStatus: Status = "active";

// Object with as const
const Role = {
  Admin: "ADMIN",
  User: "USER",
  Guest: "GUEST"
} as const;

type RoleType = typeof Role[keyof typeof Role];

// Benefits: better tree-shaking, cleaner output
```

---

## Part 5: Objects & Type Aliases

### 5.1 Object Typing

**Definition:** Defining types for object shapes.

```typescript
// Inline object type
const user: { id: number; name: string; email: string } = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"
};

// Object with method
const calculator: {
  add: (a: number, b: number) => number;
  subtract: (a: number, b: number) => number;
} = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b
};

// Nested objects
const person: {
  name: string;
  address: {
    street: string;
    city: string;
  };
} = {
  name: "Bob",
  address: {
    street: "123 Main St",
    city: "Boston"
  }
};
```

### 5.2 Optional Properties

**Definition:** Object properties that may or may not exist.

```typescript
// Optional property with ?
type User = {
  id: number;
  name: string;
  email?: string;  // optional
  phone?: string;  // optional
};

const user1: User = {
  id: 1,
  name: "Alice"
  // email and phone are optional
};

const user2: User = {
  id: 2,
  name: "Bob",
  email: "bob@example.com"
};

// Accessing optional properties
function sendEmail(user: User) {
  if (user.email) {
    // email is defined here
    console.log(`Sending to ${user.email}`);
  }
}
```

### 5.3 Readonly Properties

**Definition:** Properties that cannot be reassigned after creation.

```typescript
// Readonly properties
type Product = {
  readonly id: number;
  name: string;
  readonly createdAt: Date;
};

const product: Product = {
  id: 1,
  name: "Laptop",
  createdAt: new Date()
};

product.name = "Desktop"; // OK
// product.id = 2; // Error: Cannot assign to 'id'

// Readonly modifier on all properties
type ReadonlyUser = {
  readonly name: string;
  readonly age: number;
};

// Using Readonly utility type
type User = {
  name: string;
  age: number;
};

const user: Readonly<User> = {
  name: "Alice",
  age: 30
};

// user.name = "Bob"; // Error
```

### 5.4 Type Keyword

**Definition:** Creating reusable type aliases.

```typescript
// Basic type alias
type ID = number | string;

let userId: ID = 123;
let sessionId: ID = "abc-123";

// Object type alias
type User = {
  id: ID;
  name: string;
  email: string;
};

// Function type alias
type GreetFunction = (name: string) => string;

const greet: GreetFunction = (name) => `Hello, ${name}`;

// Union type alias
type Status = "pending" | "approved" | "rejected";

// Complex type alias
type ApiResponse<T> = {
  data: T;
  status: number;
  message: string;
};

// Intersection type alias
type Timestamp = {
  createdAt: Date;
  updatedAt: Date;
};

type UserWithTimestamp = User & Timestamp;
```

### 5.5 Nested Object Types

**Definition:** Objects containing other objects as properties.

```typescript
// Nested object type
type Address = {
  street: string;
  city: string;
  country: string;
  zipCode: string;
};

type User = {
  id: number;
  name: string;
  address: Address;
  billingAddress?: Address;
};

const user: User = {
  id: 1,
  name: "Alice",
  address: {
    street: "123 Main St",
    city: "Boston",
    country: "USA",
    zipCode: "02101"
  }
};

// Deeply nested
type Company = {
  name: string;
  headquarters: {
    address: Address;
    contact: {
      email: string;
      phone: string;
    };
  };
};

// Array of nested objects
type Order = {
  id: number;
  items: {
    productId: number;
    quantity: number;
    price: number;
  }[];
};
```

---

## Part 6: Interfaces

### 6.1 Interface Syntax

**Definition:** Defining object shapes using the interface keyword.

```typescript
// Basic interface
interface User {
  id: number;
  name: string;
  email: string;
}

const user: User = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"
};

// Interface with methods
interface Calculator {
  add(a: number, b: number): number;
  subtract(a: number, b: number): number;
}

const calc: Calculator = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b
};

// Optional properties
interface Product {
  id: number;
  name: string;
  description?: string;
}

// Readonly properties
interface Config {
  readonly apiUrl: string;
  readonly timeout: number;
}
```

### 6.2 Interface vs Type

**Comparison:**

```typescript
// Interfaces can be extended
interface Animal {
  name: string;
}

interface Dog extends Animal {
  breed: string;
}

// Types use intersection
type Animal = {
  name: string;
};

type Dog = Animal & {
  breed: string;
};

// Interfaces can be reopened (declaration merging)
interface User {
  name: string;
}

interface User {
  age: number;
}

// Merged: User has both name and age

// Types cannot be reopened
type Product = {
  name: string;
};

// type Product = { price: number }; // Error: Duplicate identifier

// Types are more flexible with unions
type ID = string | number; // OK
// interface ID = string | number; // Error

// Recommendation:
// - Use interface for object shapes and APIs
// - Use type for unions, intersections, and utilities
```

### 6.3 Extending Interfaces

**Definition:** Creating new interfaces based on existing ones.

```typescript
// Single extension
interface BaseEntity {
  id: number;
  createdAt: Date;
  updatedAt: Date;
}

interface User extends BaseEntity {
  name: string;
  email: string;
}

// Multiple extension
interface Timestamped {
  createdAt: Date;
  updatedAt: Date;
}

interface Identifiable {
  id: number;
}

interface User extends Identifiable, Timestamped {
  name: string;
  email: string;
}

// Extending and overriding
interface Animal {
  name: string;
  age: number;
}

interface Dog extends Animal {
  age: number; // OK: same type
  breed: string;
}
```

### 6.4 Function Interfaces

**Definition:** Defining function signatures using interfaces.

```typescript
// Basic function interface
interface AddFunction {
  (a: number, b: number): number;
}

const add: AddFunction = (a, b) => a + b;

// Function with properties
interface Logger {
  (message: string): void;
  level: string;
}

const logger: Logger = (message) => {
  console.log(`[${logger.level}] ${message}`);
};
logger.level = "INFO";

// Generic function interface
interface Mapper<T, U> {
  (item: T): U;
}

const toString: Mapper<number, string> = (num) => num.toString();
```

### 6.5 Index Signatures

**Definition:** Allowing dynamic property names with specific types.

```typescript
// String index signature
interface StringMap {
  [key: string]: string;
}

const colors: StringMap = {
  primary: "blue",
  secondary: "green",
  accent: "red"
};

// Number index signature
interface NumberArray {
  [index: number]: number;
}

const scores: NumberArray = [90, 85, 88];

// Mixed with known properties
interface Dictionary {
  [key: string]: any;
  count: number; // known property
}

const dict: Dictionary = {
  count: 3,
  name: "Alice",
  age: 30,
  active: true
};

// Readonly index signature
interface ReadonlyStringMap {
  readonly [key: string]: string;
}
```

### 6.6 Interfaces for APIs & DTOs

**Definition:** Using interfaces to define API request/response shapes.

```typescript
// DTO (Data Transfer Object)
interface CreateUserDto {
  name: string;
  email: string;
  password: string;
}

interface UpdateUserDto {
  name?: string;
  email?: string;
}

// API Response interfaces
interface ApiResponse<T> {
  success: boolean;
  data: T;
  message?: string;
}

interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  pageSize: number;
}

// Usage
interface User {
  id: number;
  name: string;
  email: string;
}

type UserResponse = ApiResponse<User>;
type UsersListResponse = PaginatedResponse<User>;

// Request interfaces
interface LoginRequest {
  email: string;
  password: string;
}

interface LoginResponse {
  token: string;
  user: User;
}

---
```
## Part 7: Union & Intersection Types

### 7.1 Union Types

**Definition:** A value that can be one of several types (OR logic).

```typescript
// Basic union
let id: string | number;
id = 123;        // OK
id = "abc-123";  // OK
// id = true;    // Error

// Function with union parameter
function printId(id: string | number) {
  console.log(`ID: ${id}`);
}

// Union of literals
type Status = "pending" | "approved" | "rejected";
let taskStatus: Status = "pending"; // OK
// taskStatus = "completed"; // Error

// Union with null/undefined
type MaybeString = string | null | undefined;

// Array with union types
let mixed: (string | number)[] = [1, "two", 3, "four"];

// Union of object types
type Success = { status: "success"; data: string };
type Error = { status: "error"; message: string };
type Result = Success | Error;

function handleResult(result: Result) {
  if (result.status === "success") {
    console.log(result.data);
  } else {
    console.log(result.message);
  }
}
```

### 7.2 Intersection Types

**Definition:** Combining multiple types into one (AND logic).

```typescript
// Basic intersection
type Person = {
  name: string;
  age: number;
};

type Employee = {
  employeeId: number;
  department: string;
};

type Staff = Person & Employee;

const staff: Staff = {
  name: "Alice",
  age: 30,
  employeeId: 123,
  department: "Engineering"
};

// Intersection with methods
type Loggable = {
  log(): void;
};

type Serializable = {
  serialize(): string;
};

type Entity = Loggable & Serializable;

// Multiple intersections
type Timestamped = {
  createdAt: Date;
  updatedAt: Date;
};

type Identifiable = {
  id: number;
};

type BaseEntity = Identifiable & Timestamped;

type User = BaseEntity & {
  name: string;
  email: string;
};
```

### 7.3 Discriminated Unions

**Definition:** Union types with a common discriminant property for type narrowing.

```typescript
// Basic discriminated union
type Square = {
  kind: "square";
  size: number;
};

type Rectangle = {
  kind: "rectangle";
  width: number;
  height: number;
};

type Circle = {
  kind: "circle";
  radius: number;
};

type Shape = Square | Rectangle | Circle;

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "square":
      return shape.size * shape.size;
    case "rectangle":
      return shape.width * shape.height;
    case "circle":
      return Math.PI * shape.radius ** 2;
  }
}

// API Response pattern
type SuccessResponse<T> = {
  success: true;
  data: T;
};

type ErrorResponse = {
  success: false;
  error: string;
};

type ApiResponse<T> = SuccessResponse<T> | ErrorResponse;

function handleResponse<T>(response: ApiResponse<T>) {
  if (response.success) {
    console.log(response.data);
  } else {
    console.error(response.error);
  }
}

// State machine pattern
type IdleState = { state: "idle" };
type LoadingState = { state: "loading"; progress: number };
type SuccessState = { state: "success"; data: string };
type ErrorState = { state: "error"; error: Error };

type State = IdleState | LoadingState | SuccessState | ErrorState;

function renderUI(state: State) {
  switch (state.state) {
    case "idle":
      return "Ready";
    case "loading":
      return `Loading: ${state.progress}%`;
    case "success":
      return `Data: ${state.data}`;
    case "error":
      return `Error: ${state.error.message}`;
  }
}
```

---

## Part 8: Type Narrowing

### 8.1 Typeof Narrowing

**Definition:** Using JavaScript's `typeof` operator to narrow types.

```typescript
// Basic typeof narrowing
function process(value: string | number) {
  if (typeof value === "string") {
    // value is string here
    return value.toUpperCase();
  }
  // value is number here
  return value.toFixed(2);
}

// Multiple types
function format(input: string | number | boolean) {
  if (typeof input === "string") {
    return input.trim();
  } else if (typeof input === "number") {
    return input.toFixed(2);
  } else {
    return input ? "Yes" : "No";
  }
}

// Null and undefined checking
function printLength(str: string | null | undefined) {
  if (typeof str === "string") {
    console.log(str.length);
  } else {
    console.log("No string provided");
  }
}
```

### 8.2 Instanceof Narrowing

**Definition:** Using `instanceof` to narrow class types.

```typescript
// Class instanceof narrowing
class Dog {
  bark() {
    console.log("Woof!");
  }
}

class Cat {
  meow() {
    console.log("Meow!");
  }
}

function makeSound(animal: Dog | Cat) {
  if (animal instanceof Dog) {
    animal.bark();
  } else {
    animal.meow();
  }
}

// Error handling
function handleError(error: Error | string) {
  if (error instanceof Error) {
    console.error(error.message);
    console.error(error.stack);
  } else {
    console.error(error);
  }
}

// Custom classes
class ApiError extends Error {
  constructor(public statusCode: number, message: string) {
    super(message);
  }
}

function processError(error: unknown) {
  if (error instanceof ApiError) {
    console.log(`API Error ${error.statusCode}: ${error.message}`);
  } else if (error instanceof Error) {
    console.log(`Error: ${error.message}`);
  }
}
```

### 8.3 In Operator

**Definition:** Using `in` operator to check if a property exists.

```typescript
// Property checking
type Dog = { bark: () => void };
type Cat = { meow: () => void };

function makeSound(animal: Dog | Cat) {
  if ("bark" in animal) {
    animal.bark();
  } else {
    animal.meow();
  }
}

// Optional property checking
interface User {
  name: string;
  email?: string;
}

function sendEmail(user: User) {
  if ("email" in user && user.email) {
    console.log(`Sending to ${user.email}`);
  }
}

// Discriminated unions alternative
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; size: number };

function getArea(shape: Shape) {
  if ("radius" in shape) {
    return Math.PI * shape.radius ** 2;
  }
  return shape.size * shape.size;
}
```

### 8.4 Custom Type Guards

**Definition:** Creating functions that return type predicates.

```typescript
// Basic type guard
function isString(value: unknown): value is string {
  return typeof value === "string";
}

function process(value: unknown) {
  if (isString(value)) {
    console.log(value.toUpperCase()); // value is string
  }
}

// Object type guard
interface User {
  name: string;
  email: string;
}

function isUser(obj: any): obj is User {
  return (
    typeof obj === "object" &&
    obj !== null &&
    typeof obj.name === "string" &&
    typeof obj.email === "string"
  );
}

function greetUser(data: unknown) {
  if (isUser(data)) {
    console.log(`Hello, ${data.name}`);
  }
}

// Array type guard
function isStringArray(value: unknown): value is string[] {
  return (
    Array.isArray(value) &&
    value.every(item => typeof item === "string")
  );
}

// Complex type guards
interface ApiError {
  error: string;
  code: number;
}

function isApiError(response: any): response is ApiError {
  return (
    typeof response === "object" &&
    response !== null &&
    "error" in response &&
    "code" in response &&
    typeof response.error === "string" &&
    typeof response.code === "number"
  );
}

async function fetchData(url: string) {
  const response = await fetch(url);
  const data = await response.json();
  
  if (isApiError(data)) {
    throw new Error(`API Error ${data.code}: ${data.error}`);
  }
  
  return data;
}
```

---

## Part 9: Generics

### 9.1 Generic Functions

**Definition:** Functions that work with multiple types using type parameters.

```typescript
// Basic generic function
function identity<T>(arg: T): T {
  return arg;
}

let num = identity<number>(5);
let str = identity<string>("hello");
let inferred = identity(true); // type inferred as boolean

// Generic function with array
function firstElement<T>(arr: T[]): T | undefined {
  return arr[0];
}

let first = firstElement([1, 2, 3]); // number | undefined
let firstStr = firstElement(["a", "b"]); // string | undefined

// Multiple type parameters
function pair<T, U>(first: T, second: U): [T, U] {
  return [first, second];
}

let p1 = pair<string, number>("age", 30);
let p2 = pair("name", "Alice"); // inferred

// Generic with constraints
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

let user = { name: "Alice", age: 30 };
let name = getProperty(user, "name"); // string
let age = getProperty(user, "age");   // number

// Generic callback function
function map<T, U>(arr: T[], fn: (item: T) => U): U[] {
  return arr.map(fn);
}

let numbers = [1, 2, 3];
let strings = map(numbers, n => n.toString()); // string[]

// Async generic function
async function fetchJson<T>(url: string): Promise<T> {
  const response = await fetch(url);
  return response.json();
}

interface User {
  id: number;
  name: string;
}

let user = await fetchJson<User>("/api/user");
```

### 9.2 Generic Interfaces

**Definition:** Interfaces with type parameters.

```typescript
// Basic generic interface
interface Box<T> {
  value: T;
}

let numberBox: Box<number> = { value: 123 };
let stringBox: Box<string> = { value: "hello" };

// Generic interface with methods
interface Repository<T> {
  findById(id: number): Promise<T | null>;
  findAll(): Promise<T[]>;
  save(item: T): Promise<T>;
  delete(id: number): Promise<void>;
}

// Implementation
interface User {
  id: number;
  name: string;
}

class UserRepository implements Repository<User> {
  async findById(id: number): Promise<User | null> {
    // implementation
    return null;
  }
  
  async findAll(): Promise<User[]> {
    return [];
  }
  
  async save(user: User): Promise<User> {
    return user;
  }
  
  async delete(id: number): Promise<void> {
    // implementation
  }
}

// Multiple type parameters
interface KeyValuePair<K, V> {
  key: K;
  value: V;
}

let kv: KeyValuePair<string, number> = {
  key: "age",
  value: 30
};

// Generic interface extending
interface Timestamped {
  createdAt: Date;
  updatedAt: Date;
}

interface Entity<T> extends Timestamped {
  id: number;
  data: T;
}

// API Response interface
interface ApiResponse<T> {
  success: boolean;
  data: T;
  error?: string;
}

let userResponse: ApiResponse<User> = {
  success: true,
  data: { id: 1, name: "Alice" }
};
```

### 9.3 Generic Classes

**Definition:** Classes with type parameters.

```typescript
// Basic generic class
class Container<T> {
  private value: T;
  
  constructor(value: T) {
    this.value = value;
  }
  
  getValue(): T {
    return this.value;
  }
  
  setValue(value: T): void {
    this.value = value;
  }
}

let numContainer = new Container<number>(123);
let strContainer = new Container<string>("hello");

// Generic class with multiple types
class Pair<T, U> {
  constructor(
    public first: T,
    public second: U
  ) {}
  
  getFirst(): T {
    return this.first;
  }
  
  getSecond(): U {
    return this.second;
  }
}

let pair = new Pair("name", 30);

// Generic collection class
class Collection<T> {
  private items: T[] = [];
  
  add(item: T): void {
    this.items.push(item);
  }
  
  remove(item: T): void {
    const index = this.items.indexOf(item);
    if (index > -1) {
      this.items.splice(index, 1);
    }
  }
  
  getAll(): T[] {
    return [...this.items];
  }
  
  find(predicate: (item: T) => boolean): T | undefined {
    return this.items.find(predicate);
  }
}

let numbers = new Collection<number>();
numbers.add(1);
numbers.add(2);

// Generic with static members
class Cache<T> {
  private static instances = new Map<string, any>();
  
  constructor(private key: string) {}
  
  set(value: T): void {
    Cache.instances.set(this.key, value);
  }
  
  get(): T | undefined {
    return Cache.instances.get(this.key);
  }
  
  static clear(): void {
    Cache.instances.clear();
  }
}
```

### 9.4 Generic Constraints

**Definition:** Restricting generic types to specific shapes or capabilities.

```typescript
// Constraint with extends
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

getLength("hello");     // OK: string has length
getLength([1, 2, 3]);   // OK: array has length
// getLength(123);      // Error: number doesn't have length

// Constraining to object keys
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

let user = { name: "Alice", age: 30 };
getProperty(user, "name"); // OK
// getProperty(user, "email"); // Error: "email" not in user

// Multiple constraints
interface Lengthwise {
  length: number;
}

interface Printable {
  print(): void;
}

function process<T extends Lengthwise & Printable>(item: T): void {
  console.log(item.length);
  item.print();
}

// Constraining to constructor
function create<T>(constructor: new () => T): T {
  return new constructor();
}

class User {
  name = "Alice";
}

let user = create(User); // User instance

// Generic constraint with interface
interface HasId {
  id: number;
}

function findById<T extends HasId>(items: T[], id: number): T | undefined {
  return items.find(item => item.id === id);
}

// Constraint with default type
interface Container<T = string> {
  value: T;
}

let c1: Container = { value: "hello" }; // defaults to string
let c2: Container<number> = { value: 123 };

// Recursive constraint
type JSONValue =
  | string
  | number
  | boolean
  | null
  | JSONValue[]
  | { [key: string]: JSONValue };

function parseJSON<T extends JSONValue>(json: string): T {
  return JSON.parse(json);
}
```

---

## Part 10: Utility Types

### 10.1 Partial

**Definition:** Makes all properties optional.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

// All properties become optional
type PartialUser = Partial<User>;
// Equivalent to:
// {
//   id?: number;
//   name?: string;
//   email?: string;
//   age?: number;
// }

// Usage: Update functions
function updateUser(id: number, updates: Partial<User>) {
  // Can update any combination of properties
}

updateUser(1, { name: "Bob" });
updateUser(2, { email: "new@email.com", age: 31 });

// Nested Partial
interface Company {
  name: string;
  address: {
    street: string;
    city: string;
  };
}

type PartialCompany = Partial<Company>;
// address is optional, but its properties are still required if provided

// Deep Partial (custom)
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

type DeepPartialCompany = DeepPartial<Company>;
// Now address.street and address.city are also optional
```

### 10.2 Required

**Definition:** Makes all properties required.

```typescript
interface User {
  id: number;
  name: string;
  email?: string;
  phone?: string;
}

// All properties become required
type RequiredUser = Required<User>;
// Equivalent to:
// {
//   id: number;
//   name: string;
//   email: string;
//   phone: string;
// }

// Usage: Validation
function validateUser(user: Required<User>): boolean {
  // Now we know email and phone definitely exist
  return user.email.includes("@") && user.phone.length > 0;
}

// Form submission
interface FormData {
  username?: string;
  password?: string;
  email?: string;
}

function submitForm(data: Required<FormData>) {
  // All fields are guaranteed to be present
  console.log(data.username, data.password, data.email);
}
```

### 10.3 Pick

**Definition:** Create a type by picking specific properties.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
  createdAt: Date;
}

// Pick only needed properties
type UserPreview = Pick<User, "id" | "name" | "email">;
// Equivalent to:
// {
//   id: number;
//   name: string;
//   email: string;
// }

// Usage: API responses (exclude sensitive data)
function getUserPreview(id: number): UserPreview {
  // Return user without password and createdAt
  return {
    id: 1,
    name: "Alice",
    email: "alice@example.com"
  };
}

// Form DTOs
type LoginDto = Pick<User, "email" | "password">;

function login(credentials: LoginDto) {
  // Only email and password
}

// Pick single property
type UserId = Pick<User, "id">;
```

### 10.4 Omit

**Definition:** Create a type by omitting specific properties.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
  createdAt: Date;
}

// Omit sensitive/internal fields
type PublicUser = Omit<User, "password">;
// Equivalent to:
// {
//   id: number;
//   name: string;
//   email: string;
//   createdAt: Date;
// }

// Omit multiple properties
type UserDto = Omit<User, "password" | "createdAt">;

// Usage: Update DTOs (exclude id)
type UpdateUserDto = Omit<User, "id" | "createdAt">;

function updateUser(id: number, data: UpdateUserDto) {
  // data doesn't have id or createdAt
}

// Combined with Partial
type UpdateUserInput = Partial<Omit<User, "id">>;

// Omit from Pick
type UserInfo = Pick<User, "name" | "email" | "password">;
type UserInfoWithoutPassword = Omit<UserInfo, "password">;
```

### 10.5 Readonly

**Definition:** Makes all properties read-only.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

// All properties become readonly
type ReadonlyUser = Readonly<User>;
// Equivalent to:
// {
//   readonly id: number;
//   readonly name: string;
//   readonly email: string;
// }

const user: ReadonlyUser = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"
};

// user.name = "Bob"; // Error: Cannot assign to 'name'

// Usage: Configuration
interface Config {
  apiUrl: string;
  timeout: number;
  retries: number;
}

const config: Readonly<Config> = {
  apiUrl: "https://api.example.com",
  timeout: 5000,
  retries: 3
};

// config.apiUrl = "new url"; // Error

// Readonly arrays
let numbers: readonly number[] = [1, 2, 3];
// numbers.push(4); // Error
// numbers[0] = 10; // Error

// ReadonlyArray utility
let names: ReadonlyArray<string> = ["Alice", "Bob"];
```

### 10.6 Record

**Definition:** Create an object type with specific keys and value type.

```typescript
// Basic Record
type Role = "admin" | "user" | "guest";
type Permissions = Record<Role, string[]>;

const permissions: Permissions = {
  admin: ["read", "write", "delete"],
  user: ["read", "write"],
  guest: ["read"]
};

// Record with string keys
type StringRecord = Record<string, number>;

const ages: StringRecord = {
  alice: 30,
  bob: 25,
  charlie: 35
};

// Record for configuration
type Environment = "development" | "staging" | "production";
type EnvConfig = Record<Environment, { apiUrl: string; debug: boolean }>;

const envConfig: EnvConfig = {
  development: {
    apiUrl: "http://localhost:3000",
    debug: true
  },
  staging: {
    apiUrl: "https://staging.example.com",
    debug: true
  },
  production: {
    apiUrl: "https://api.example.com",
    debug: false
  }
};

// Record with number keys
type NumericRecord = Record<number, string>;

const statusCodes: NumericRecord = {
  200: "OK",
  404: "Not Found",
  500: "Server Error"
};

// Partial Record (some keys optional)
type PartialPermissions = Partial<Record<Role, string[]>>;
```

### 10.7 ReturnType

**Definition:** Extract the return type of a function.

```typescript
// Basic usage
function getUser() {
  return {
    id: 1,
    name: "Alice",
    email: "alice@example.com"
  };
}

type User = ReturnType<typeof getUser>;
// User is { id: number; name: string; email: string; }

// With async functions
async function fetchData() {
  return { data: "hello", status: 200 };
}

type FetchResult = ReturnType<typeof fetchData>;
// FetchResult is Promise<{ data: string; status: number; }>

// Unwrap Promise
type UnwrappedFetchResult = Awaited<ReturnType<typeof fetchData>>;
// { data: string; status: number; }

// Generic function
function createPair<T, U>(first: T, second: U) {
  return { first, second };
}

type PairResult = ReturnType<typeof createPair<string, number>>;
// { first: string; second: number; }

// Function type
type MyFunction = () => { x: number; y: number };
type Result = ReturnType<MyFunction>;
// { x: number; y: number; }
```

### 10.8 Parameters

**Definition:** Extract parameter types from a function as a tuple.

```typescript
// Basic usage
function greet(name: string, age: number) {
  return `Hello ${name}, you are ${age} years old`;
}

type GreetParams = Parameters<typeof greet>;
// [name: string, age: number]

// Destructuring parameters
const [name, age] = params as GreetParams;

// Usage in wrapper functions
function loggedGreet(...args: Parameters<typeof greet>) {
  console.log("Calling greet with:", args);
  return greet(...args);
}

// Generic function parameters
function map<T, U>(arr: T[], fn: (item: T) => U): U[] {
  return arr.map(fn);
}

type MapParams = Parameters<typeof map<number, string>>;
// [arr: number[], fn: (item: number) => string]

// Constructor parameters
class User {
  constructor(
    public name: string,
    public email: string,
    public age: number
  ) {}
}

type UserConstructorParams = ConstructorParameters<typeof User>;
// [name: string, email: string, age: number]

function createUser(...args: UserConstructorParams) {
  return new User(...args);
}
```
---
