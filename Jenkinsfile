
// pipeline {
//     agent { docker { image 'python:3.10.1-alpine' } }
//     stages {
//         stage('build') {
//             steps {
//                 sh 'python --version'
//             }
//         }
//     }
// }

node('docker') {
    stage('Build') {
        docker.image('python:3.10.1-alpine').inside {
            sh 'python --version'
        }
    }
}