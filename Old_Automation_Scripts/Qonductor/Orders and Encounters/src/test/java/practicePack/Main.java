package practicePack;



	public class Main {
	    public void main(String[] args) {
	        Animal animal = new Animal();
	        animal.makeSound();  // Output: Animal makes a sound

	        Dog dog = new Dog();
	        dog.makeSound();     // Output: Dog barks
	    }
		public class Animal {
		    public void makeSound() {
		        System.out.println("Animal makes a sound");
		    }
		}

		public class Dog extends Animal {
		    @Override
		    public void makeSound() {
		        System.out.println("Dog barks");
		    }
		}
	}
	
