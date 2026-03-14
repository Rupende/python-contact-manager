def save_contacts(contacts, filename):

    with open(filename, "w") as file:

        for contact in contacts:

            line = contact["name"] + "," + contact["phone"] + "\n"

            file.write(line)


def load_contacts(contacts, filename):

    try:

        with open(filename, "r") as file:

            for line in file:

                name, phone = line.strip().split(",")

                contacts.append({
                    "name": name,
                    "phone": phone
                })

    except FileNotFoundError:

        pass