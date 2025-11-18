package com.example;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

import spoon.Launcher;
import spoon.reflect.CtModel;
import spoon.reflect.declaration.CtType;

public class Main {

    public static void main(String[] args) throws IOException {
        Launcher launcher = new Launcher();
        try {
            File allfile = new File("C:\\Users\\syuuj\\spoonTEXT\\demo\\first.txt");
            BufferedReader allreader = new BufferedReader(new FileReader(allfile));
            String str;
            while ((str = allreader.readLine()) != null) {
                launcher.addInputResource(str);
            }
            File diffFile = new File("C:\\Users\\syuuj\\spoonTEXT\\demo\\first.txt");   //後ほどlogを読み取ったファイルに置き換える
            BufferedReader diffReader = new BufferedReader(new FileReader(diffFile));
            List<Path> diffFileList=new ArrayList<>();
            while((str=diffReader.readLine())!=null){
                diffFileList.add(Paths.get(str));                                          //１つ目の要素はgitのhash値　それ以降の要素が変更のあったファイル名
            }

        } catch (IOException e) {
            System.out.println("失敗" + e.getMessage());
        }

        launcher.getEnvironment().setCommentEnabled(false);
        launcher.getEnvironment().setAutoImports(true);
        CtModel model = launcher.buildModel();
        Visitor visitor = new Visitor();

        for (CtType<?> clazz : model.getAllTypes()) {
            clazz.accept(visitor);
        }
        visitor.excuteMetrics();
        visitor.printCSV(args[0]);
    }

    private static List<String> addJarSourceFile(Path path) throws IOException {
        List<String> JarFile;
        try (Stream<Path> paths = Files.walk(path)) {
            JarFile = paths.filter(p -> p.toString().endsWith(".jar")).map(p -> p.toString()).toList();
        }
        return JarFile;
    }

}
/*    
    //JarFile=filterConflictingJars(JarFile);
    private static List<String> filterConflictingJars(List<String> jars) {
        List<String> safe = new ArrayList<>();
        for (String jar : jars) {
            try (JarFile jf = new JarFile(jar)) {
                boolean hasConflict = jf.stream().anyMatch(entry -> {
                    String name = entry.getName();
                    return name.startsWith("org/w3c/dom")
                            || name.startsWith("javax/xml/")
                            || name.startsWith("org/xml/sax/");
                });
                if (!hasConflict) {
                    safe.add(jar);
                } else {
                    System.out.println("Conflict : " + jar);
                }
            } catch (Exception e) {
            }
        }
        return safe;
    }*/
