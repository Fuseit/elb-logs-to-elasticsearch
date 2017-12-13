branchName = env.JOB_NAME.split('/')[(env.JOB_NAME.split('/').length) - 1]
if (branchName == 'master') {
  node('coreos') { //node type defined in Jenkins configuration
    withSlackNotify( //wrapper to catch buils result and notify slck
        {
          stage('Pre') {
            own
            checkout scm
          }
          stage('Build') {
            buildAndPush()
          }
        },
        'ci-notifications', //slack channel
        'fuse_report_service', //name of the bot
    )
  }
} else {
  println "Nothing to do, this image is built just from the master branch"
}