# Python OOP Real-World Example: Library Management System
# =======================================================
#
# This file demonstrates a comprehensive real-world example of Object-Oriented Programming
# in Python by implementing a Library Management System. The system allows for managing
# books, patrons, and the borrowing process with various features like search, notifications,
# and analytics.
#
# This example demonstrates:
# - Class hierarchies and inheritance
# - Encapsulation and data hiding
# - Polymorphism
# - Abstract classes and interfaces
# - Property decorators
# - Magic methods
# - Static and class methods
# - Exception handling
# - Design patterns (Observer pattern for notifications)

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import uuid
import json
from typing import List, Dict, Optional, Set, Tuple, Any


# ===============================
# Abstract Base Classes
# ===============================

class LibraryItem(ABC):
    """
    Abstract base class for all items that can be stored in the library.
    Defines the common interface that all library items must implement.
    """

    def __init__(self, title: str, item_id: Optional[str] = None):
        self._title = title
        self._item_id = item_id if item_id else str(uuid.uuid4())
        self._checked_out = False
        self._added_date = datetime.now()

    @property
    def title(self) -> str:
        return self._title

    @property
    def item_id(self) -> str:
        return self._item_id

    @property
    def is_checked_out(self) -> bool:
        return self._checked_out

    @property
    def added_date(self) -> datetime:
        return self._added_date

    @abstractmethod
    def get_details(self) -> Dict[str, Any]:
        """Return a dictionary with all item details"""
        pass

    def check_out(self) -> bool:
        """Mark the item as checked out"""
        if self._checked_out:
            return False
        self._checked_out = True
        return True

    def check_in(self) -> bool:
        """Mark the item as checked in"""
        if not self._checked_out:
            return False
        self._checked_out = False
        return True

    def __str__(self) -> str:
        status = "Checked Out" if self._checked_out else "Available"
        return f"{self._title} ({status})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(title='{self._title}', item_id='{self._item_id}')"


class Person(ABC):
    """
    Abstract base class for all people in the library system.
    """

    def __init__(self, name: str, email: str, person_id: Optional[str] = None):
        self._name = name
        self._email = email
        self._person_id = person_id if person_id else str(uuid.uuid4())
        self._registered_date = datetime.now()

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def person_id(self) -> str:
        return self._person_id

    @property
    def registered_date(self) -> datetime:
        return self._registered_date

    @abstractmethod
    def get_details(self) -> Dict[str, Any]:
        """Return a dictionary with all person details"""
        pass

    def __str__(self) -> str:
        return f"{self._name} ({self._email})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self._name}', email='{self._email}', person_id='{self._person_id}')"


# ===============================
# Concrete Library Item Classes
# ===============================

class Book(LibraryItem):
    """
    Represents a physical book in the library.
    """

    def __init__(self, title: str, author: str, isbn: str, 
                 pages: int, publisher: str, year: int, 
                 item_id: Optional[str] = None):
        super().__init__(title, item_id)
        self._author = author
        self._isbn = isbn
        self._pages = pages
        self._publisher = publisher
        self._year = year
        self._genre: Optional[str] = None

    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def pages(self) -> int:
        return self._pages

    @property
    def publisher(self) -> str:
        return self._publisher

    @property
    def year(self) -> int:
        return self._year

    @property
    def genre(self) -> Optional[str]:
        return self._genre

    @genre.setter
    def genre(self, value: str) -> None:
        self._genre = value

    def get_details(self) -> Dict[str, Any]:
        """Return a dictionary with all book details"""
        return {
            'id': self._item_id,
            'title': self._title,
            'author': self._author,
            'isbn': self._isbn,
            'pages': self._pages,
            'publisher': self._publisher,
            'year': self._year,
            'genre': self._genre,
            'checked_out': self._checked_out,
            'added_date': self._added_date.isoformat()
        }

    def __str__(self) -> str:
        status = "Checked Out" if self._checked_out else "Available"
        return f"{self._title} by {self._author} ({status})"


class DVD(LibraryItem):
    """
    Represents a DVD in the library.
    """

    def __init__(self, title: str, director: str, runtime: int, 
                 release_year: int, item_id: Optional[str] = None):
        super().__init__(title, item_id)
        self._director = director
        self._runtime = runtime  # in minutes
        self._release_year = release_year
        self._actors: List[str] = []

    @property
    def director(self) -> str:
        return self._director

    @property
    def runtime(self) -> int:
        return self._runtime

    @property
    def release_year(self) -> int:
        return self._release_year

    @property
    def actors(self) -> List[str]:
        return self._actors.copy()  # Return a copy to prevent external modification

    def add_actor(self, actor: str) -> None:
        """Add an actor to the DVD's actor list"""
        if actor not in self._actors:
            self._actors.append(actor)

    def get_details(self) -> Dict[str, Any]:
        """Return a dictionary with all DVD details"""
        return {
            'id': self._item_id,
            'title': self._title,
            'director': self._director,
            'runtime': self._runtime,
            'release_year': self._release_year,
            'actors': self._actors,
            'checked_out': self._checked_out,
            'added_date': self._added_date.isoformat()
        }

    def __str__(self) -> str:
        status = "Checked Out" if self._checked_out else "Available"
        return f"{self._title} directed by {self._director} ({status})"


class EBook(Book):
    """
    Represents an electronic book in the library.
    Inherits from Book but adds file format and size.
    """

    def __init__(self, title: str, author: str, isbn: str, 
                 pages: int, publisher: str, year: int, 
                 file_format: str, size_mb: float,
                 item_id: Optional[str] = None):
        super().__init__(title, author, isbn, pages, publisher, year, item_id)
        self._file_format = file_format
        self._size_mb = size_mb
        self._download_count = 0

    @property
    def file_format(self) -> str:
        return self._file_format

    @property
    def size_mb(self) -> float:
        return self._size_mb

    @property
    def download_count(self) -> int:
        return self._download_count

    def download(self) -> None:
        """Simulate downloading the ebook and increment the download counter"""
        self._download_count += 1
        print(f"Downloading {self._title} in {self._file_format} format...")

    def get_details(self) -> Dict[str, Any]:
        """Return a dictionary with all ebook details"""
        details = super().get_details()
        details.update({
            'file_format': self._file_format,
            'size_mb': self._size_mb,
            'download_count': self._download_count
        })
        return details

    def __str__(self) -> str:
        status = "Checked Out" if self._checked_out else "Available"
        return f"{self._title} by {self._author} ({self._file_format}, {status})"


# ===============================
# Concrete Person Classes
# ===============================

class Patron(Person):
    """
    Represents a library patron who can borrow items.
    """

    def __init__(self, name: str, email: str, 
                 address: str, phone: str,
                 person_id: Optional[str] = None):
        super().__init__(name, email, person_id)
        self._address = address
        self._phone = phone
        self._borrowed_items: Dict[str, datetime] = {}  # item_id -> due_date
        self._fine_amount = 0.0

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        self._phone = value

    @property
    def borrowed_items(self) -> Dict[str, datetime]:
        return self._borrowed_items.copy()  # Return a copy to prevent external modification

    @property
    def fine_amount(self) -> float:
        return self._fine_amount

    def borrow_item(self, item: LibraryItem, due_days: int = 14) -> bool:
        """
        Borrow a library item with a specified due date.
        Returns True if successful, False otherwise.
        """
        if item.is_checked_out or item.item_id in self._borrowed_items:
            return False

        if item.check_out():
            due_date = datetime.now() + timedelta(days=due_days)
            self._borrowed_items[item.item_id] = due_date
            return True
        return False

    def return_item(self, item: LibraryItem) -> Tuple[bool, float]:
        """
        Return a borrowed item and calculate any late fees.
        Returns a tuple of (success, fine_amount).
        """
        if item.item_id not in self._borrowed_items:
            return False, 0.0

        due_date = self._borrowed_items[item.item_id]
        del self._borrowed_items[item.item_id]
        item.check_in()

        # Calculate late fee if any (e.g., $0.25 per day)
        fine = 0.0
        if datetime.now() > due_date:
            days_late = (datetime.now() - due_date).days
            fine = days_late * 0.25
            self._fine_amount += fine

        return True, fine

    def pay_fine(self, amount: float) -> bool:
        """Pay a specified amount of the patron's fine"""
        if amount <= 0 or amount > self._fine_amount:
            return False

        self._fine_amount -= amount
        return True

    def get_details(self) -> Dict[str, Any]:
        """Return a dictionary with all patron details"""
        return {
            'id': self._person_id,
            'name': self._name,
            'email': self._email,
            'address': self._address,
            'phone': self._phone,
            'registered_date': self._registered_date.isoformat(),
            'borrowed_items': {item_id: due_date.isoformat() 
                              for item_id, due_date in self._borrowed_items.items()},
            'fine_amount': self._fine_amount
        }


class Librarian(Person):
    """
    Represents a librarian who manages the library.
    """

    def __init__(self, name: str, email: str, 
                 employee_id: str, department: str,
                 person_id: Optional[str] = None):
        super().__init__(name, email, person_id)
        self._employee_id = employee_id
        self._department = department
        self._admin_access = False

    @property
    def employee_id(self) -> str:
        return self._employee_id

    @property
    def department(self) -> str:
        return self._department

    @property
    def admin_access(self) -> bool:
        return self._admin_access

    @admin_access.setter
    def admin_access(self, value: bool) -> None:
        self._admin_access = value

    def get_details(self) -> Dict[str, Any]:
        """Return a dictionary with all librarian details"""
        return {
            'id': self._person_id,
            'name': self._name,
            'email': self._email,
            'employee_id': self._employee_id,
            'department': self._department,
            'admin_access': self._admin_access,
            'registered_date': self._registered_date.isoformat()
        }


# ===============================
# Observer Pattern for Notifications
# ===============================

class Observer(ABC):
    """
    Observer interface for the Observer pattern.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """Method called when the observed subject changes"""
        pass


class Subject(ABC):
    """
    Subject interface for the Observer pattern.
    """

    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Attach an observer to this subject"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detach an observer from this subject"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, message: str) -> None:
        """Notify all observers"""
        for observer in self._observers:
            observer.update(message)


class EmailNotifier(Observer):
    """
    Concrete observer that sends email notifications.
    """

    def __init__(self, email_address: str):
        self.email_address = email_address

    def update(self, message: str) -> None:
        """Send an email notification (simulated)"""
        print(f"Sending email to {self.email_address}: {message}")


class SMSNotifier(Observer):
    """
    Concrete observer that sends SMS notifications.
    """

    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def update(self, message: str) -> None:
        """Send an SMS notification (simulated)"""
        print(f"Sending SMS to {self.phone_number}: {message}")


# ===============================
# Main Library System
# ===============================

class LibrarySystem(Subject):
    """
    Main class that manages the entire library system.
    Implements the Subject interface to notify observers about events.
    """

    def __init__(self, name: str):
        super().__init__()
        self._name = name
        self._items: Dict[str, LibraryItem] = {}
        self._patrons: Dict[str, Patron] = {}
        self._librarians: Dict[str, Librarian] = {}
        self._transaction_log: List[Dict[str, Any]] = []

    @property
    def name(self) -> str:
        return self._name

    # Item management methods

    def add_item(self, item: LibraryItem) -> bool:
        """Add a new item to the library"""
        if item.item_id in self._items:
            return False

        self._items[item.item_id] = item
        self._log_transaction("add_item", {"item_id": item.item_id})
        self.notify(f"New item added: {item.title}")
        return True

    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the library"""
        if item_id not in self._items:
            return False

        item = self._items[item_id]
        if item.is_checked_out:
            return False

        del self._items[item_id]
        self._log_transaction("remove_item", {"item_id": item_id})
        self.notify(f"Item removed: {item.title}")
        return True

    def get_item(self, item_id: str) -> Optional[LibraryItem]:
        """Get an item by its ID"""
        return self._items.get(item_id)

    def search_items(self, **kwargs) -> List[LibraryItem]:
        """
        Search for items based on various criteria.
        Example: search_items(title="Python", checked_out=False)
        """
        results = []

        for item in self._items.values():
            match = True

            for key, value in kwargs.items():
                # Special case for checking if an item is checked out
                if key == "checked_out":
                    if item.is_checked_out != value:
                        match = False
                        break
                # Check if the attribute exists and matches
                elif hasattr(item, key):
                    item_value = getattr(item, key)
                    # Case-insensitive string search
                    if isinstance(item_value, str) and isinstance(value, str):
                        if value.lower() not in item_value.lower():
                            match = False
                            break
                    # Exact match for other types
                    elif item_value != value:
                        match = False
                        break
                else:
                    match = False
                    break

            if match:
                results.append(item)

        return results

    # Patron management methods

    def register_patron(self, patron: Patron) -> bool:
        """Register a new patron"""
        if patron.person_id in self._patrons:
            return False

        self._patrons[patron.person_id] = patron
        self._log_transaction("register_patron", {"patron_id": patron.person_id})
        self.notify(f"New patron registered: {patron.name}")
        return True

    def get_patron(self, patron_id: str) -> Optional[Patron]:
        """Get a patron by their ID"""
        return self._patrons.get(patron_id)

    # Librarian management methods

    def add_librarian(self, librarian: Librarian) -> bool:
        """Add a new librarian"""
        if librarian.person_id in self._librarians:
            return False

        self._librarians[librarian.person_id] = librarian
        self._log_transaction("add_librarian", {"librarian_id": librarian.person_id})
        return True

    def get_librarian(self, librarian_id: str) -> Optional[Librarian]:
        """Get a librarian by their ID"""
        return self._librarians.get(librarian_id)

    # Borrowing and returning methods

    def check_out_item(self, patron_id: str, item_id: str, due_days: int = 14) -> bool:
        """Check out an item to a patron"""
        patron = self.get_patron(patron_id)
        item = self.get_item(item_id)

        if not patron or not item:
            return False

        if patron.borrow_item(item, due_days):
            self._log_transaction("check_out", {
                "patron_id": patron_id,
                "item_id": item_id,
                "due_days": due_days
            })
            self.notify(f"{patron.name} has borrowed: {item.title}")
            return True
        return False

    def return_item(self, patron_id: str, item_id: str) -> Tuple[bool, float]:
        """Return an item and calculate any late fees"""
        patron = self.get_patron(patron_id)
        item = self.get_item(item_id)

        if not patron or not item:
            return False, 0.0

        success, fine = patron.return_item(item)
        if success:
            self._log_transaction("return_item", {
                "patron_id": patron_id,
                "item_id": item_id,
                "fine": fine
            })

            message = f"{patron.name} has returned: {item.title}"
            if fine > 0:
                message += f" with a late fee of ${fine:.2f}"
            self.notify(message)

            return True, fine
        return False, 0.0

    # Analytics methods

    def get_checked_out_items(self) -> List[LibraryItem]:
        """Get all currently checked out items"""
        return [item for item in self._items.values() if item.is_checked_out]

    def get_available_items(self) -> List[LibraryItem]:
        """Get all available items"""
        return [item for item in self._items.values() if not item.is_checked_out]

    def get_overdue_items(self) -> Dict[str, List[Tuple[LibraryItem, datetime]]]:
        """
        Get all overdue items grouped by patron.
        Returns a dictionary mapping patron_id to a list of (item, due_date) tuples.
        """
        overdue_items: Dict[str, List[Tuple[LibraryItem, datetime]]] = {}
        now = datetime.now()

        for patron_id, patron in self._patrons.items():
            patron_overdue = []

            for item_id, due_date in patron.borrowed_items.items():
                if now > due_date:
                    item = self.get_item(item_id)
                    if item:
                        patron_overdue.append((item, due_date))

            if patron_overdue:
                overdue_items[patron_id] = patron_overdue

        return overdue_items

    def get_popular_items(self, limit: int = 10) -> List[Tuple[LibraryItem, int]]:
        """
        Get the most popular items based on checkout frequency.
        Returns a list of (item, checkout_count) tuples.
        """
        # Count checkouts from transaction log
        checkout_counts: Dict[str, int] = {}

        for transaction in self._transaction_log:
            if transaction["type"] == "check_out":
                item_id = transaction["details"]["item_id"]
                checkout_counts[item_id] = checkout_counts.get(item_id, 0) + 1

        # Get the items and sort by checkout count
        popular_items = []
        for item_id, count in checkout_counts.items():
            item = self.get_item(item_id)
            if item:
                popular_items.append((item, count))

        # Sort by count (descending) and limit results
        popular_items.sort(key=lambda x: x[1], reverse=True)
        return popular_items[:limit]

    # Utility methods

    def _log_transaction(self, transaction_type: str, details: Dict[str, Any]) -> None:
        """Log a transaction in the system"""
        transaction = {
            "timestamp": datetime.now().isoformat(),
            "type": transaction_type,
            "details": details
        }
        self._transaction_log.append(transaction)

    def export_data(self, filename: str) -> bool:
        """Export library data to a JSON file"""
        try:
            data = {
                "name": self._name,
                "items": {item_id: item.get_details() for item_id, item in self._items.items()},
                "patrons": {patron_id: patron.get_details() for patron_id, patron in self._patrons.items()},
                "librarians": {lib_id: lib.get_details() for lib_id, lib in self._librarians.items()},
                "transactions": self._transaction_log
            }

            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)

            return True
        except Exception as e:
            print(f"Error exporting data: {e}")
            return False

    def __str__(self) -> str:
        return f"{self._name} Library System with {len(self._items)} items and {len(self._patrons)} patrons"


# ===============================
# Usage Example
# ===============================

def main():
    """
    Demonstrate the library system with a complete example.
    """
    # Create the library system
    library = LibrarySystem("City Public Library")

    # Create some books
    book1 = Book(
        title="Python Programming",
        author="John Smith",
        isbn="978-1234567890",
        pages=350,
        publisher="Tech Books",
        year=2020
    )
    book1.genre = "Computer Science"

    book2 = Book(
        title="Data Science Essentials",
        author="Jane Doe",
        isbn="978-0987654321",
        pages=420,
        publisher="Data Press",
        year=2019
    )
    book2.genre = "Computer Science"

    # Create an ebook
    ebook1 = EBook(
        title="Web Development with Django",
        author="Bob Johnson",
        isbn="978-5678901234",
        pages=280,
        publisher="Code Books",
        year=2021,
        file_format="PDF",
        size_mb=15.7
    )
    ebook1.genre = "Computer Science"

    # Create a DVD
    dvd1 = DVD(
        title="The Python Documentary",
        director="Alice Brown",
        runtime=120,
        release_year=2018
    )
    dvd1.add_actor("David Python")
    dvd1.add_actor("Sarah Coder")

    # Add items to the library
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(ebook1)
    library.add_item(dvd1)

    # Create patrons
    patron1 = Patron(
        name="Michael Johnson",
        email="michael@example.com",
        address="123 Main St",
        phone="555-1234"
    )

    patron2 = Patron(
        name="Emily Davis",
        email="emily@example.com",
        address="456 Oak Ave",
        phone="555-5678"
    )

    # Register patrons
    library.register_patron(patron1)
    library.register_patron(patron2)

    # Create a librarian
    librarian = Librarian(
        name="Sarah Wilson",
        email="sarah@library.com",
        employee_id="L001",
        department="Fiction"
    )
    librarian.admin_access = True

    # Add librarian
    library.add_librarian(librarian)

    # Set up notifications
    email_notifier = EmailNotifier("admin@library.com")
    sms_notifier = SMSNotifier("555-ADMIN")

    library.attach(email_notifier)
    library.attach(sms_notifier)

    # Perform some operations
    print("\n=== Checking out items ===")
    library.check_out_item(patron1.person_id, book1.item_id)
    library.check_out_item(patron2.person_id, dvd1.item_id)

    # Search for items
    print("\n=== Searching for Python books ===")
    python_items = library.search_items(title="Python")
    for item in python_items:
        print(f"Found: {item}")

    # Get checked out items
    print("\n=== Currently checked out items ===")
    for item in library.get_checked_out_items():
        print(f"Checked out: {item}")

    # Return an item
    print("\n=== Returning an item ===")
    success, fine = library.return_item(patron1.person_id, book1.item_id)
    if success:
        print(f"Return successful. Fine: ${fine:.2f}")

    # Download an ebook
    print("\n=== Downloading an ebook ===")
    ebook1.download()

    # Export library
    library.export_data("library_data.json")
    print("\n=== Library data exported to library_data.json ===")

# Run the demonstration
if __name__ == "__main__":
    main()
