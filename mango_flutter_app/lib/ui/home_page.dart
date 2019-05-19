import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  static String tag = 'home-page';

  @override
  Widget build(BuildContext context) {
    final alucard = Hero(
      tag: 'hero',
      child: Padding(
        padding: EdgeInsets.all(16.0),
        child: CircleAvatar(
          radius: 72.0,
          backgroundColor: Colors.transparent,
          backgroundImage: AssetImage('assets/mango.png'),
        ),
      ),
    );

    final welcome = Padding(
      padding: EdgeInsets.all(8.0),
      child: Text(
        'Welcome Alucard',
        style: TextStyle(fontSize: 28.0, color: Colors.white),
      ),
    );

    final lorem = Padding(
      padding: EdgeInsets.all(8.0),
      child: Text(
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec hendrerit condimentum mauris id tempor. Praesent eu commodo lacus. Praesent eget mi sed libero eleifend tempor. Sed at fringilla ipsum. Duis malesuada feugiat urna vitae convallis. Aliquam eu libero arcu.',
        style: TextStyle(fontSize: 16.0, color: Colors.white),
      ),
    );

    final body = Container(
      width: MediaQuery.of(context).size.width,
      padding: EdgeInsets.all(28.0),
      decoration: BoxDecoration(
        gradient: LinearGradient(colors: [
          Colors.blue,
          Colors.lightBlueAccent,
        ]),
      ),
      child: Column(
        children: <Widget>[alucard, welcome, lorem],
      ),
    );

    return Scaffold(
      appBar: new AppBar(
        title: new Text('Mango')
      ),
      drawer: new Drawer(
          child: new ListView(
            children: <Widget> [
              new UserAccountsDrawerHeader(
                accountName: Text("Nikos Monahogios"),
                accountEmail: Text("nikos13@hotmail.com"),
                currentAccountPicture: CircleAvatar(
                    backgroundColor: Theme.of(context).platform == TargetPlatform.iOS
                      ? Colors.blue : Colors.white,
                    child: Text(
                      "NM",
                      style: TextStyle(fontSize: 35),
                    )
                ),
          ),
              new ListTile(
                leading: Icon(Icons.work),
                title: new Text('Jobs'),
                onTap: () {},
              ),
              new ListTile(
                leading: Icon(Icons.insert_drive_file),
                title: new Text('Applications'),
                onTap: () {},
              ),
              new ListTile(
                leading: Icon(Icons.account_circle),
                title: new Text('My Profile'),
                onTap: () {},
              ),
              new Divider(),
              new ListTile(
                leading: Icon(Icons.info),
                title: new Text('About'),
                onTap: () {},
              ),
              new ListTile(
                leading: Icon(Icons.help),
                title: new Text('Help'),
                onTap: () {},
              ),
              new ListTile(
                leading: Icon(Icons.exit_to_app),
                title: new Text('Logout'),
                onTap: () {},
              ),
            ],
          )
      ),
      body: body,
    );
  }
}
