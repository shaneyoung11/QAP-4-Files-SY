const MotelCustomer = {
  firstName: "Chuck",
  lastName: "Norris",
  birthDate: "March 10",
  birthYear: 1940,
  gender: "Android",

  roomPreferences: [
    " Ocean View",
    " Basement Celler",
    " Cardboard Box",
    " Executive Suite",
  ],

  paymentMethod: "Bitcoin",

  mailingAddress: {
    street: "666 Sesame Street",
    city: "Paradise",
    province: "NL",
    postalCode: "H0H 0H0",
  },

  phoneNumber: "7097388888",
  interestingFact: [
    "He doesn't do push-ups; he pushes the Earth down",
    " can divide by zero",
    " can slam a revolving door",
    " counted to infinity; twice",
  ],

  checkInDate: {
    day: 30,
    month: 3,
    year: 2024,
  },

  checkOutDate: {
    day: 5,
    month: 4,
    year: 2024,
  },

  getAge: function () {
    const today = new Date();
    return today.getFullYear() - this.birthYear;
  },

  getStayDuration: function () {
    const checkIn = new Date(
      this.checkInDate.year,
      this.checkInDate.month,
      this.checkInDate.day
    );
    const checkOut = new Date(
      this.checkOutDate.year,
      this.checkOutDate.month,
      this.checkOutDate.day
    );
    const difference = Math.abs(checkOut - checkIn);
    const days = Math.ceil(difference / (1000 * 60 * 60 * 24));
    return days;
  },
};

const custDesc = `${MotelCustomer.firstName} ${MotelCustomer.lastName} is a loyal customer to Sleep - Tite Motel. He lives on ${MotelCustomer.mailingAddress.street}, which is in ${MotelCustomer.mailingAddress.city}, ${MotelCustomer.mailingAddress.province}. ${MotelCustomer.firstName}'s preferred rooms are${MotelCustomer.roomPreferences} and their birthday is ${MotelCustomer.birthDate}, ${MotelCustomer.birthYear}. Some interesting facts about ${MotelCustomer.firstName}: ${MotelCustomer.interestingFact}. Their preferred method of payment is ${MotelCustomer.paymentMethod}. Thank you for staying at Sleep - Tite!`;

document.body.innerHTML = custDesc;
