import sqlite3
import os

def explore_database(db_path):
    """Explore and display the contents of a SQLite database"""
    
    if not os.path.exists(db_path):
        print(f"Database file '{db_path}' not found!")
        return
    
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print(f"Successfully connected to database: {db_path}")
        print("=" * 50)
        
        # Get list of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        if not tables:
            print("No tables found in the database.")
            return
        
        print(f"Found {len(tables)} table(s):")
        for table in tables:
            print(f"  - {table[0]}")
        print()
        
        # Explore each table
        for table in tables:
            table_name = table[0]
            print(f"Table: {table_name}")
            print("-" * 30)
            
            # Get table schema
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            print("Columns:")
            for col in columns:
                col_id, col_name, col_type, not_null, default_val, pk = col
                print(f"  {col_name} ({col_type})")
            print()
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            row_count = cursor.fetchone()[0]
            print(f"Row count: {row_count}")
            
            # Show sample data (first 5 rows)
            if row_count > 0:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
                rows = cursor.fetchall()
                
                print("Sample data (first 5 rows):")
                for i, row in enumerate(rows, 1):
                    print(f"  Row {i}: {row}")
            print()
        
        conn.close()
        print("Database exploration completed!")
        
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Explore the database
    explore_database("listOfTasks.db")
