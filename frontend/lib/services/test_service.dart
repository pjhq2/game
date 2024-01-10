import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:frontend/models/weapon_model.dart';

class TestService {
  final String apiUrl = 'http://127.0.0.1:8000/api/v1/';

  Future<WeaponModel> fetchWeaponData() async {
    final response = await http.get(Uri.parse(apiUrl));

    if (response.statusCode == 200) {
      final body = response.bodyBytes;
      final data = jsonDecode(utf8.decode(body));
      print(data[0]);
      return data[0];
    } else {
      throw Exception('Failed to load weapons');
    }
  }
}