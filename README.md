# **Digital Catalogue System**

This is an easy-to-use, web-based digital catalogue for online registration and management of suppliers, RFQs and quotations.

---

## **Introduction**

Digital Catalogue System is accessible through a web browser such as:

* Google Chrome
* Safari 
* Mozilla Firefox
* Internet Explorer etc).

Customers who visit the site can register as a supplier, view issued RFQs and respond to them through Quotations. To use the system, customers must first ***sign up*** tto create an account.

The system will provide a basic view where the customer can interact with different modules (e.g., Supplier registration, RFQs and Quotations). 

The system is developed to send email notifications to appropriate individuals at different stages. This helps to ensure timely and efficient registration of suppliers and management of RFQs and quotations.

---

## **Installation**

Digital Catalogue System is built on the [Frappe Framework](https://frappeframework.com/ "Frappe Site"), a full-stack, open source, web development framework written in Python & JavaScript. The framework is ***generic*** and can be used to build database driven apps. ***MariaDB*** is the default database for the framework.

To install Digital Catalogue System, you will have to install [Frappe-Bench](https://frappeframework.com/docs/v13/user/en/installation "Frappe Bench Installation"), a command-line package and site manager for the Frappe Framework.

>For more details, read the Bench ***README***.

After installing Frappe Bench, you will have to initialise a bench directory with the Frappe Framework using the following command:

```bench
bench init digital_catalogue
```

Next, change the directory to ***digital_catalogue*** and download the Digital Catalogue app with the following command:

```bench
cd digital_catalogue

bench get-app digital_catalogue https://github.com/IoT-Communications/Digital-Catalogue.git
```

Create a new site to install the app by running the command:

```bench
bench new-site digital-catalogue.example.com
```

This will create a new folder in your ***/sites*** directory and create a new database for this site.

Next, install the Digital Catalogue app in this site by running the command:

```bench
bench --site digital-catalogue.example.com install-app digital_catalogue
```

To run the app locally, you must start the bench service with the command:

```bench
bench start
```

At this point, the Digital Catalogue app is installed and listening on port 8000. 

You can now fire up your browser by clicking [this link](http://localhost:8000/ "Login Screen") and you should see the login screen. 

Login as Administrator and use the password you set at the time of creating the site ***(digital-catalogue.example.com)***.

---

## **License**

MIT
