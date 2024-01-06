import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<dynamic> users = [];
  List<dynamic> tests = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          title: const Text('Rest API Call')
      ),
      body: ListView.builder(
          itemCount: users.length,
          itemBuilder: (context, index){
            final user = users[index];
            final email = user['email'];
            final name = user['name']['first'];
            // final imageUrl = user['picture']['thumbnail'];
            return ListTile(
              leading: ClipRRect(
                borderRadius: BorderRadius.circular(100),
                child: Text('${index + 1}'),
                // child: Image.network(imageUrl),
              ),
              title: Text(email),
              subtitle: Text(name.toString()),
            );
          }),
      floatingActionButton: FloatingActionButton(
        onPressed: fetchTests,
      ),
      bottomNavigationBar: BottomAppBar(
        color: Colors.lightGreen,
        child: ListView.builder(
            itemCount: tests.length,
            itemBuilder: (context, index){
            final test = tests[index];
            final id = test['id'];
            final title = test['title'];
            final content = test['content'];
            // final created_at = test['created_on'];
            // final updated_at = test['updated_on'];
            return ListTile(
              leading: Text(id),
              title: Text(title),
              subtitle: Text(content)
          );
        }),
      )
    );
  }

  void fetchUsers() async {
    print('fetchUsers called');
    const url = 'https://randomuser.me/api/?results=100';
    final uri = Uri.parse(url);
    final response = await http.get(uri);
    final body = response.body;
    final json = jsonDecode(body);
    setState(() {
        users = json['results'];
    });
    print('fetch completed');
  }

  void fetchTests() async {
    print('fetchTest called');
    const url = 'http://127.0.0.1:8000/api/v1/';
    final uri = Uri.parse(url);
    final response = await http.get(uri);
    final body = response.body;
    final json = jsonDecode(body);
    setState(() {
      tests = json['results'];
    });
    print('fetch completed');
  }
}
