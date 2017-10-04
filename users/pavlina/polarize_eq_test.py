
import visa
visa.log_to_screen()
rm = visa.ResourceManager()
print(rm.list_resources())
