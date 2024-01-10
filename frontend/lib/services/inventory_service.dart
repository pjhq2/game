import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:frontend/models/inventory_model.dart';

class InventoryService {
  final String apiUrl = 'http://127.0.0.1:8000/api/v1/inventory';

  Future<List<InventoryModel>> fetchInventories() async {
    final response = await http.get(Uri.parse(apiUrl));

    if (response.statusCode == 200) {
      final body = response.bodyBytes;
      List<dynamic> data = jsonDecode(utf8.decode(body));
      print(data);
      return data.map((json) => InventoryModel.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load inventories');
    }
  }
}