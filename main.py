import em05

def main():
    dev = em05.EM05(debug=True)  # Enable debug mode for detailed logging

    smss = dev.sms_list_all()
    print(f"SMS List: {smss}")

    resp = dev.sms_send(phone_number='10086', text='Hello, this is a test message!')

    print(f"SMS Send Response: {resp}")

if __name__ == "__main__":
    main()