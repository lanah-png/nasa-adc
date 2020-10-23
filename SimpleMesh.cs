using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class SimpleMesh : MonoBehaviour
{
    //fields
    public Vector3[] vertices;
    public int[] triangles; //need to set this up
    Vector2[] newUV;  //need to set this up (less important??)
    Mesh mesh;
    string path = "Assets/smalldata.txt"; //change to whatever file location is 


    void Start()
    {
        
        //mesh set up
        CreateShape(); 
        
        mesh = new Mesh();

        mesh.vertices = vertices;
        mesh.uv = newUV;
        mesh.triangles = triangles;

        GetComponent<MeshFilter>().mesh = mesh;
        mesh.RecalculateNormals();
    }

    // Update is called once per frame
    void Update()
    {
    }

    void CreateShape()
    {
        //file reading stuff
        StreamReader reader = new StreamReader(path); 
        string s = reader.ReadToEnd();
        reader.Close();

        //separate txt file by linebreaks
        string[] lines = s.Split("\n"[0]);

        //assign points to vertices
        vertices = new Vector3[lines.Length];

        for(int i = 0; i < vertices.Length; i++) {
            //split line by comma
            string[] values = lines[i].Split(","[0]);
            
            Debug.Log(lines[i]); //testing stuff lol

            vertices[i] = new Vector3(float.Parse(values[0]), float.Parse(values[1]), float.Parse(values[2]));
        }
        
        //triangle stuff i hope
        triangles = new int[vertices.Length - vertices.Length%3];
		for (int i = 0; i < triangles.Length / 6; i++) {
            triangles[i * 6 + 0] = i * 2;
            triangles[i * 6 + 1] = i * 2 + 1;
            triangles[i * 6 + 2] = i * 2 + 2;
 
            triangles[i * 6 + 3] = i * 2 + 2;
            triangles[i * 6 + 4] = i * 2 + 1;
            triangles[i * 6 + 5] = i * 2 + 3;
        }


    }

    void UpdateMesh()
    {
        mesh.Clear();

        mesh.vertices = vertices;
        mesh.triangles = triangles;
    }

}
