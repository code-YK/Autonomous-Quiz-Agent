import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { CheckCircle2, AlertCircle, RefreshCw } from "lucide-react"

interface ValidationSectionProps {
  validationPassed: boolean
  validationFeedback: string
  retryCount: number
}

export function ValidationSection({ validationPassed, validationFeedback, retryCount }: ValidationSectionProps) {
  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 mb-4">
        {validationPassed ? (
          <CheckCircle2 className="h-5 w-5 text-accent" />
        ) : (
          <AlertCircle className="h-5 w-5 text-destructive" />
        )}
        <h3 className="text-lg font-semibold text-foreground">Validation Results</h3>
      </div>

      <div className="grid gap-4 md:grid-cols-3">
        <Card className="border-border">
          <CardHeader className="pb-3">
            <CardDescription className="text-xs">Status</CardDescription>
          </CardHeader>
          <CardContent>
            <Badge
              variant="outline"
              className={
                validationPassed
                  ? "bg-green-500/10 text-green-700 dark:text-green-400 border-green-500/20"
                  : "bg-red-500/10 text-red-700 dark:text-red-400 border-red-500/20"
              }
            >
              {validationPassed ? "Passed" : "Failed"}
            </Badge>
          </CardContent>
        </Card>

        <Card className="border-border">
          <CardHeader className="pb-3">
            <CardDescription className="text-xs">Retry Count</CardDescription>
          </CardHeader>
          <CardContent className="flex items-center gap-2">
            <RefreshCw className="h-4 w-4 text-muted-foreground" />
            <span className="text-2xl font-bold text-foreground">{retryCount}</span>
          </CardContent>
        </Card>

        <Card className="border-border md:col-span-1">
          <CardHeader className="pb-3">
            <CardDescription className="text-xs">Quality Score</CardDescription>
          </CardHeader>
          <CardContent>
            <span className="text-2xl font-bold text-foreground">{validationPassed ? "High" : "Low"}</span>
          </CardContent>
        </Card>
      </div>

      <Card className="border-border">
        <CardHeader>
          <CardTitle className="text-base">Validation Feedback</CardTitle>
          <CardDescription>Detailed analysis from the validation agent</CardDescription>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-foreground leading-relaxed whitespace-pre-wrap">{validationFeedback}</p>
        </CardContent>
      </Card>
    </div>
  )
}
