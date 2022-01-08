using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

public class GradeSheet
{
	public static GradeSheet Deserialize(string filePath)
    {
		JsonSerializerOptions options = new JsonSerializerOptions() { WriteIndented = true };
		try {
			string jsonContent = File.ReadAllText(filePath);
			Console.WriteLine(jsonContent);
			GradeSheet sheet = JsonSerializer.Deserialize<GradeSheet>(jsonContent);
			return sheet;
		} catch(FileLoadException e) {
			Console.WriteLine(e.Message);
			return new GradeSheet("", Groups.beginner);
		}
    }

	public string Name { get; set; }
	public enum Groups
	{
		beginner,
		intermediate,
		advanced,
	}

	public Groups group;

	public Dictionary<string, double> grades;
	public GradeSheet(string name, Groups group)
	{
		grades = new Dictionary<string, double>();
		this.Name = name;
		this.group = group;
	}

	public double AvarageGrade()
    {
		double sum = 0;
		int number = 0;
		foreach(KeyValuePair<string, double> kvp in this.grades) {
			sum += kvp.Value;
			number++;
		}
		return sum / number;
    }
	public void Serialize(string filePath)
    {
		JsonSerializerOptions options = new JsonSerializerOptions() { WriteIndented = true };
		string objAsJson = JsonSerializer.Serialize(this, options);
		try {
			File.WriteAllText(filePath, objAsJson);
		} catch(UnauthorizedAccessException e) {
			Console.WriteLine(e.Message);
		}
    }
	
}