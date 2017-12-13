@Library('Fuse-jenkins@improvement/better-docker-management') _

branchName = env.JOB_NAME.split('/')[(env.JOB_NAME.split('/').length) - 1]

node('coreos') { //node type defined in Jenkins configuration
  withSlackNotify( //wrapper to catch buils result and notify slck
      {
        stage('Pre') {
          own
          checkout scm
        }
        stage('Build') {
          tag = buildAndPush()
        }

        if (branchName == 'master') {
          stage('Create secret') {
            kubernetesSecret(
                'dev',
                'tools',
                'elb-logs'
            )
          }
          stage('Deploy') {
            kubernetesDeploy(
                true, //approval needed
                'dev', //cluster
                'tools', //namespace
                'deploy/elb-logs.yml', //deploy file
                tag //image tag
            )
          }
        }
      },
      'ci-notifications', //slack channel
      'jenkins', //name of the bot
  )
}
